from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db

from app.models.user import User

from app.crud.resume_crud import get_resume

from app.schemas.ai_schema import (
    AIAnalysisRequest,
    AIAnalysisResponse,
)

from app.services.ai_service import analyze_resume

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/analyze",
    response_model=AIAnalysisResponse,
)
def analyze(
    request: AIAnalysisRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    resume = get_resume(
        db=db,
        resume_id=request.resume_id,
        user_id=current_user.id,
    )

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    result = analyze_resume(
        resume.extracted_text,
        request.job_description,
    )

    return result