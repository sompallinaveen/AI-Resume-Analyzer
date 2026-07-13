from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db

from app.models.user import User

from app.crud.resume_crud import get_resume
from app.crud.job_crud import get_job

from app.schemas.matching_schema import MatchResponse

from app.services.matching_service import calculate_similarity

router = APIRouter(
    prefix="/matching",
    tags=["AI Matching"],
)


@router.get(
    "/{resume_id}/{job_id}",
    response_model=MatchResponse,
)
def match_resume(
    resume_id: int,
    job_id: int,
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

    job = get_job(
        db=db,
        job_id=job_id,
        user_id=current_user.id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    score = calculate_similarity(
        resume.extracted_text,
        job.description,
    )

    return MatchResponse(
        resume_id=resume.id,
        job_id=job.id,
        similarity_score=score,
    )