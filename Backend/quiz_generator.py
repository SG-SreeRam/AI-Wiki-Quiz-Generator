import json
import re
from llm import generate_quiz_from_text

def extract_json(text):
    """
    Extract first JSON object from text safely
    """
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("LLM did not return JSON")

    return match.group(0)

def generate_quiz(text):
    raw = generate_quiz_from_text(text)

    json_text = extract_json(raw)

    return json.loads(json_text)
