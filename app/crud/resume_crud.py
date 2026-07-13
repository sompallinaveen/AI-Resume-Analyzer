from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.core.logger import logger

def create_resume(
    db: Session,
    original_filename: str,
    stored_filename: str,
    file_path: str,
    extracted_text: str,
) -> Resume:
    logger.info(f"Saving resume: {original_filename}")

    resume = Resume(
        original_filename=original_filename,
        stored_filename=stored_filename,
        file_path=file_path,
        extracted_text=extracted_text,
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    logger.info(f"Resume saved successfully with ID: {resume.id}")

    return resume


def get_resume(db: Session, resume_id: int) -> Resume | None:
    logger.info(f"Fetching resume with ID: {resume_id}")

    return (
        db.query(Resume)
        .filter(Resume.id == resume_id)
        .first()
    )


def get_all_resumes(db: Session):
    logger.info("Fetching all resumes")

    return db.query(Resume).all()