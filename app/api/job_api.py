from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.crud.job_crud import create_job, get_jobs
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.job_schema import JobCreate, JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post(
    "/",
    response_model=JobResponse,
)
def create_job_description(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_job(
        db=db,
        user_id=current_user.id,
        title=job.title,
        company=job.company,
        description=job.description,
    )


@router.get(
    "/",
    response_model=list[JobResponse],
)
def get_my_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_jobs(
        db=db,
        user_id=current_user.id,
    )