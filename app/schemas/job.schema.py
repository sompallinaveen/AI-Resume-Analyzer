from datetime import datetime

from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    title: str
    company: str | None = None
    description: str


class JobResponse(BaseModel):
    id: int
    title: str
    company: str | None = None
    description: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )