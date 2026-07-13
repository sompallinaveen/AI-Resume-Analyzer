from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    original_filename = Column(
        String,
        nullable=False,
    )

    stored_filename = Column(
        String,
        nullable=False,
    )

    file_path = Column(
        String,
        nullable=False,
    )

    extracted_text = Column(Text)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    owner = relationship(
        "User",
        back_populates="resumes",
    )