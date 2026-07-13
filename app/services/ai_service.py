from app.services.matching_service import calculate_similarity
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

    return {
        "similarity_score": similarity,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }