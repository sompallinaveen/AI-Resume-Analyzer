from groq import Groq

from app.core.config import settings
from app.parsers.llm_parser import parse_llm_response
from app.prompts.resume_prompt import build_resume_prompt

client = Groq(
    api_key=settings.GROQ_API_KEY,
)


def analyze_resume(
    resume_text: str,
    job_description: str,
) -> dict:

    prompt = build_resume_prompt(
        resume_text,
        job_description,
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.3,
    )

    content = response.choices[0].message.content

    return parse_llm_response(content)