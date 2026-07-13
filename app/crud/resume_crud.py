from sqlalchemy.orm import Session

from app.models.resume import Resume


def create_resume(
    db: Session,
    user_id: int,
    original_filename: str,
    stored_filename: str,
    file_path: str,
    extracted_text: str,
) -> Resume:
    """
    Create a new resume for a user.
    """

    resume = Resume(
        user_id=user_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        file_path=file_path,
        extracted_text=extracted_text,
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_resume(
    db: Session,
    resume_id: int,
    user_id: int,
):
    """
    Get a resume owned by the user.
    """

    return (
        db.query(Resume)
        .filter(
            Resume.id == resume_id,
            Resume.user_id == user_id,
        )
        .first()
    )


def get_all_resumes(
    db: Session,
    user_id: int,
):
    """
    Get all resumes belonging to a user.
    """

    return (
        db.query(Resume)
        .filter(
            Resume.user_id == user_id
        )
        .order_by(Resume.uploaded_at.desc())
        .all()
    )