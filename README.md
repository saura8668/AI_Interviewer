# AI Interviewer

AI Interviewer is a Python-based application designed to assist in generating and analyzing interview questions and answers using AI. It leverages Pydantic for schema validation, MongoDB for data storage, and integrates with an AI service (e.g., GPT) for generating and scoring responses.

## Features

- **Question Generation**: Automatically generate interview questions based on user designation, experience, and skills.
- **Answer Analysis**: Analyze user-provided answers to questions and score them on a scale of 0 to 10.
- **Dynamic Questioning**: Generate follow-up questions based on previous answers.
- **User Reports**: Fetch a detailed report of all questions and answers for a specific user.

## Technologies Used

- **Python**: Core programming language.
- **Pydantic**: For schema validation.
- **MongoDB**: Database for storing questions, answers, and scores.
- **AI Integration**: Uses an AI service (e.g., GPT) for generating and analyzing content.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai_interviewer.git
   cd ai_interviewer