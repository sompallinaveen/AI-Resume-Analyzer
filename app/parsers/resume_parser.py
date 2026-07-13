import re

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

PHONE_REGEX = r"(?:\+91[- ]?)?[6-9]\d{9}"


def parse_resume(text: str):

    email = re.search(EMAIL_REGEX, text)
    phone = re.search(PHONE_REGEX, text)

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    name = lines[0] if lines else None

    return {
        "name": name,
        "email": email.group() if email else None,
        "phone": phone.group() if phone else None
    }