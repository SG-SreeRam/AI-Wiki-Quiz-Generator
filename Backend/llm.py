import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Try Gemini 2.5 Flash (free tier for some accounts)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz_from_text(text):
    prompt = f"""
Generate 5 quiz questions from the following Wikipedia content.

Each question must include:
- question
- 4 options
- correct answer
- difficulty
- explanation

Also include:
- related_topics (array of Wikipedia topics)

Return ONLY valid JSON in this format:
{{
  "quiz": [
    {{
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "answer": "...",
      "difficulty": "easy|medium|hard",
      "explanation": "..."
    }}
  ],
  "related_topics": ["..."]
}}

Content:
{text}
"""

    response = model.generate_content(prompt)

    return response.text
