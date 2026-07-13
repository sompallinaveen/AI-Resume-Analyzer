from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ats_service import calculate_ats_score

router = APIRouter(
    prefix="/ats",
    tags=["ATS"]
)


class ATSRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/score")
def ats_score(request: ATSRequest):
    return calculate_ats_score(
        request.resume_text,
        request.job_description
    )