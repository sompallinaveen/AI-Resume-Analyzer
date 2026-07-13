from pathlib import Path
from typing import Any
from app.core.logger import logger
from app.parsers.resume_parser import parse_resume
from app.utils.pdf_utils import extract_text_from_pdf
from app.utils.skill_extractor import extract_skills


def process_resume(file_path: Path) -> dict[str, Any]:
    try:
        logger.info("Extracting text from PDF...")

        text = extract_text_from_pdf(file_path)

        logger.info("Parsing resume...")

        parsed = parse_resume(text)

        logger.info("Extracting skills...")

        skills = extract_skills(text)

        logger.info("Resume processed successfully.")

        return {
            "characters": len(text),
            "words": len(text.split()),
            "text": text,
            "parsed_data": parsed,
            "skills": skills,
        }

    except Exception as e:
        logger.error(f"Resume processing failed: {e}")
        raise