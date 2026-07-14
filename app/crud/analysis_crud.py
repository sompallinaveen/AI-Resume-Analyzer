from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.analysis import Analysis


def create_analysis(
    db: Session,
    user_id: int,
    resume_id: int,
    ats_score: float,
):
    analysis = Analysis(
        user_id=user_id,
        resume_id=resume_id,
        ats_score=ats_score,
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis


def get_total_analyses(
    db: Session,
    user_id: int,
):
    return (
        db.query(Analysis)
        .filter(Analysis.user_id == user_id)
        .count()
    )


def get_average_ats(
    db: Session,
    user_id: int,
):
    average = (
        db.query(func.avg(Analysis.ats_score))
        .filter(Analysis.user_id == user_id)
        .scalar()
    )

    if average is None:
        return 0

    return round(float(average), 2)