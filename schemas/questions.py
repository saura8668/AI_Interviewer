from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FirstQuestionRequestSchema(BaseModel):
    userID:str
    designation:str
    experience:str
    skills:List[str]

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

