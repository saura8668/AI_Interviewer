from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Note(BaseModel):
    title: str
    content: str
    created_at: Optional[datetime] = None  # Timestamp for when the note was created
    updated_at: Optional[datetime] = None  # Timestamp for when the note was last updated