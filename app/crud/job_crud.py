from sqlalchemy.orm import Session

from app.models.job import Job


def create_job(
    db: Session,
    user_id: int,
    title: str,
    company: str | None,
    description: str,
):
    job = Job(
        user_id=user_id,
        title=title,
        company=company,
        description=description,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_jobs(
    db: Session,
    user_id: int,
):
    return (
        db.query(Job)
        .filter(Job.user_id == user_id)
        .all()
    )

def get_job(
    db: Session,
    job_id: int,
    user_id: int,
):
    return (
        db.query(Job)
        .filter(
            Job.id == job_id,
            Job.user_id == user_id,
        )
        .first()
    )

def get_job(
    db: Session,
    job_id: int,
    user_id: int,
):
    return (
        db.query(Job)
        .filter(
            Job.id == job_id,
            Job.user_id == user_id,
        )
        .first()
    )