from pathlib import Path
import shutil
import uuid

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends,
)
from sqlalchemy.orm import Session

from app.core.config import UPLOAD_DIR
from app.core.security import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.resume_schema import (
    ResumeUploadResponse,
    ResumeResponse,
)
from app.services.resume_service import process_resume
from app.crud.resume_crud import (
    create_resume,
    get_resume,
    get_all_resumes,
    delete_resume,
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)

# Create upload directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "/upload",
    response_model=ResumeUploadResponse,
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    # Generate unique filename
    extension = Path(file.filename).suffix
    stored_filename = f"{uuid.uuid4()}{extension}"

    # Full path to save the file
    file_path = UPLOAD_DIR / stored_filename

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process resume
    result = process_resume(file_path)

    # Save metadata
    saved_resume = create_resume(
        db=db,
        user_id=current_user.id,
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path=str(file_path),
        extracted_text=result["text"],
    )


    return {
        "resume_id": saved_resume.id,
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "characters": result["characters"],
        "words": result["words"],
        "parsed_data": result["parsed_data"],
        "skills": result["skills"],
    }


@router.get(
    "/{resume_id}",
    response_model=ResumeResponse,
)
def get_resume_by_id(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    resume = get_resume(
        db=db,
        resume_id=resume_id,
        user_id=current_user.id,
    )

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    return resume


@router.get(
    "",
    response_model=list[ResumeResponse],
)
def get_all_uploaded_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_resumes(
        db=db,
        user_id=current_user.id,
    )

@router.delete("/{resume_id}")
def delete_uploaded_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    deleted = delete_resume(
        db=db,
        resume_id=resume_id,
        user_id=current_user.id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    return {
        "message": "Resume deleted successfully"
    }