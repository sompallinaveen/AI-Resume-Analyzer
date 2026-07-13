from app.utils.skill_extractor import extract_skills


def calculate_ats_score(resume_text: str, job_description: str):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched = sorted(set(resume_skills) & set(jd_skills))
    missing = sorted(set(jd_skills) - set(resume_skills))

    score = 0

    if jd_skills:
        score = round((len(matched) / len(jd_skills)) * 100, 2)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "resume_skills": resume_skills,
        "job_skills": jd_skills
    }