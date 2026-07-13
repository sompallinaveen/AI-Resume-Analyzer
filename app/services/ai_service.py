from app.services.matching_service import calculate_similarity
from app.services.llm_service import analyze_resume as llm_analyze_resume
from app.utils.skill_extractor import extract_skills


def analyze_resume(
    resume_text: str,
    job_description: str,
):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matched_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills.difference(resume_skills)
    )

    similarity = calculate_similarity(
        resume_text,
        job_description,
    )

    try:
        ai_feedback = llm_analyze_resume(
            resume_text,
            job_description,
        )
    except Exception:
        feedback = (
            "AI feedback is currently unavailable."
        )

    return {
        "similarity_score": round(similarity, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        **ai_feedback,
    }