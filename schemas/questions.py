from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FirstQuestionRequestSchema(BaseModel):
    designation:str
    experience:str
    techStack:str

    class Config:
        extra = "forbid"  # Forbid extra fields

class QuestionRequestSchema(BaseModel):
    userID: str
    qid: str
    question: str
    answer: str

    class Config:
        extra = "forbid"  # Forbid extra fields

class QuestionResponseSchema(BaseModel):
    userID: str
    qid: str
    question: str
    answer: str

    class Config:
        extra = "forbid"  # Forbid extra fields

