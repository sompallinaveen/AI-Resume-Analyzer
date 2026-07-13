from pydantic import BaseModel


class AIAnalysisRequest(BaseModel):
    resume_id: int
    job_description: str


class AIAnalysisResponse(BaseModel):
    similarity_score: float
    matched_skills: list[str]
    missing_skills: list[str]

    overall_feedback: str
    strengths: list[str]
    weaknesses: list[str]
    resume_improvements: list[str]
    interview_questions: list[str]