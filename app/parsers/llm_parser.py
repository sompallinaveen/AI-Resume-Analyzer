import json
import re


def parse_llm_response(response_text: str) -> dict:
    """
    Parse the JSON response returned by the LLM.

    Handles:
    - Plain JSON
    - JSON inside ```json ... ``` code blocks
    - Extra whitespace

    Raises:
        ValueError: If valid JSON cannot be extracted.
    """

    response_text = response_text.strip()

    # Remove Markdown code fences if present
    response_text = re.sub(
        r"^```json\s*",
        "",
        response_text,
        flags=re.IGNORECASE,
    )

    response_text = re.sub(
        r"\s*```$",
        "",
        response_text,
    )

    try:
        return json.loads(response_text)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON returned by LLM:\n{response_text}"
        ) from e