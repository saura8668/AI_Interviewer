from config.db import client
from models.questions import Question
from schemas.questions import FirstQuestionRequestSchema, QuestionRequestSchema, QuestionResponseSchema
from services.gpt_service import generate

async def fetchQuestion(request: FirstQuestionRequestSchema | QuestionRequestSchema, id: str) -> QuestionResponseSchema:
    # Generate a question using Gemini API
    prompt = ""

    if id == "0":  # Assuming "0" indicates generating a new question
        if isinstance(request, FirstQuestionRequestSchema):
            prompt = f"Generate a question for {request.designation} with {request.experience} experience in {request.skills}. Give only the question."
        else:
            raise ValueError("Invalid request type for generating a question.")
    else:  # Assuming non-zero ID indicates analyzing an answer
        if isinstance(request, QuestionRequestSchema):
            # Save the answer to the database with score
            prompt = f"Analyze this answer given by user - {request.answer} with corresponding question - {request.question}. Then score the answer on a scale of 0 to 10. Give only the score."
            score = float(generate(prompt))
            question_data = client.questionsDB.question.find_one({"qid": request.qid})
            if not question_data:
                raise ValueError("Question not found in the database.")
            question_data["score"] = score
            question_data["answer"] = request.answer
            client.questionsDB.question.update_one({"qid": request.qid}, {"$set": question_data})

            # Generate a new question based on the previous answer
            if id !=-1:
                return QuestionResponseSchema(
                    userID="",
                    qid="",
                    question="",
                    answer=""
                )
            prompt = f"Generate a new question based on this answer - {request.answer} with corresponding question - {request.question}. Give only the question."
        else:
            raise ValueError("Invalid request type for analyzing an answer.")

    question_text = generate(prompt)

    # Create a Question instance
    question = Question(
        userID=request.userID,  # Replace with actual user ID if available
        question=question_text,
        answer="",
        score=0.0
    )

    # Store the question in the database
    client.questionsDB.question.insert_one(question.model_dump())

    # Return the response schema
    return QuestionResponseSchema(
        userID=question.userID,
        qid=question.qid,
        question=question.question,
        answer=question.answer
    )
