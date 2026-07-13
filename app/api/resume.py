from pathlib import Path
import shutil
import uuid
from typing import List
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends,
)
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.config import UPLOAD_DIR
from app.database.dependencies import get_db
from app.models.resume import Resume
from app.services.resume_service import process_resume

from app.crud.resume_crud import (
    create_resume,
    get_resume,
    get_all_resumes,
)
from app.schemas.resume_schema import (
    ResumeUploadResponse,
    ResumeResponse,
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

# Create upload directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "/upload",
    response_model=ResumeUploadResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Generate unique filename
    extension = Path(file.filename).suffix
    stored_filename = f"{uuid.uuid4()}{extension}"

    # Full path to save the file
    file_path = UPLOAD_DIR / stored_filename

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process resume (extract text, parse details, skills, etc.)
    result = process_resume(file_path)

    # Save metadata to database
    saved_resume = create_resume(
        db=db,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path=str(file_path),
        extracted_text=result["text"]
    )

    # Response
    return {
        "resume_id": saved_resume.id,
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "characters": result["characters"],
        "words": result["words"],
        "parsed_data": result["parsed_data"],
        "skills": result["skills"]
    }


@router.get("/{resume_id}")
def get_resume_by_id(
    resume_id: int,
    db: Session = Depends(get_db),
):
    resume = get_resume(db, resume_id)

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


@router.get("/")
def get_all_uploaded_resumes(
    db: Session = Depends(get_db),
):
    return get_all_resumes(db)
