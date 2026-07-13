from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ParsedData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class ResumeUploadResponse(BaseModel):
    resume_id: int
    message: str
    filename: str

    characters: int
    words: int

    parsed_data: ParsedData

    skills: List[str]

class ResumeResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    file_path: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
