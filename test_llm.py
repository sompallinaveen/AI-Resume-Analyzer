from app.services.llm_service import analyze_resume

resume = """
Python
FastAPI
SQL
Git
Machine Learning
"""

job = """
Looking for a Backend Developer.

Required Skills:
- Python
- FastAPI
- SQL
- Docker
- AWS
"""

print(
    analyze_resume(
        resume,
        job,
    )
)