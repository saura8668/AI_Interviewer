from fastapi import APIRouter,Request
from schemas.questions import FirstQuestionRequestSchema, QuestionRequestSchema, QuestionResponseSchema
from services.questions_service import fetchQuestion, fetchUserReport
from models.questions import Question
# from services.notes_service import get_all_notes


router = APIRouter()

@router.post("/questions/{id}", response_model=QuestionResponseSchema)
async def question(request: FirstQuestionRequestSchema | QuestionRequestSchema, id: str):
    return await fetchQuestion(request,id)

@router.get("/report/{userID}", response_model=list[Question])
async def report(userID: str):
    return await fetchUserReport(userID)

