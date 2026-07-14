from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.dependencies import get_db

from app.models.user import User

from app.crud.resume_crud import get_all_resumes
from app.crud.analysis_crud import (
    get_total_analyses,
    get_average_ats,
)

from app.schemas.dashboard_schema import DashboardStats

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/stats",
    response_model=DashboardStats,
)
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    resumes = get_all_resumes(
        db=db,
        user_id=current_user.id,
    )

    return {
        "total_resumes": len(resumes),
        "total_analyses": get_total_analyses(
            db,
            current_user.id,
        ),
        "average_ats": get_average_ats(
            db,
            current_user.id,
        ),
    }