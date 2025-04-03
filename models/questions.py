from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Question(BaseModel):
    userID: str
    qid: str = Field(default_factory=lambda: str(uuid.uuid4()))  # Generate a unique key
    question: str
    answer: str
    score: float
    # created_at: Optional[datetime] = None  # Timestamp for when the note was created
    # updated_at: Optional[datetime] = None  # Timestamp for when the note was last updated