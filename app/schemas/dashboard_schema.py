from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_resumes: int
    total_analyses: int
    average_ats: float