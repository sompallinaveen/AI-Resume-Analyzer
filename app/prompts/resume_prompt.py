def build_resume_prompt(
    resume_text: str,
    job_description: str,
):
    return f"""
You are an expert ATS reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.
Do not wrap the JSON in ```.

Return exactly this structure:

{{
  "overall_feedback": "",
  "strengths": [],
  "weaknesses": [],
  "resume_improvements": [],
  "interview_questions": []
}}
"""