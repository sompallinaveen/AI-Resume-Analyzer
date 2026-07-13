from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from app.database.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    original_filename = Column(String(255), nullable=False)

    stored_filename = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    extracted_text = Column(Text, nullable=False)

    ats_score = Column(Float, default=0.0)

    status = Column(String(20), default="processed")

    uploaded_at = Column(DateTime, default=datetime.utcnow)