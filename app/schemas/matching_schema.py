from pydantic import BaseModel


class MatchResponse(BaseModel):
    resume_id: int
    job_id: int
    similarity_score: float