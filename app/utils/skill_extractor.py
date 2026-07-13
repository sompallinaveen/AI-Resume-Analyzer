import re
from pathlib import Path

SKILLS_FILE = Path("data/skills.txt")

with open(SKILLS_FILE, "r", encoding="utf-8") as f:
    SKILLS = [skill.strip() for skill in f]


def extract_skills(text: str):
    found = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, flags=re.IGNORECASE):
            found.append(skill)

    return sorted(set(found))