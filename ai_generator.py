import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# ===============================
# 🧠 QUESTION GENERATOR
# ===============================

def generate_questions(stream, course, specialization, year, difficulty):

    prompt = f"""
You are an expert academic question generator.

Generate exactly 5 multiple-choice questions (MCQs).

STRICT RULES:
- Must strictly match the domain
- Do NOT generate generic science questions
- Use specialization deeply
- Year must affect difficulty depth

CONTEXT:
Stream: {stream}
Course: {course}
Specialization: {specialization}
Year: {year}
Difficulty: {difficulty}

DOMAIN GUIDE:
- Computer Science → programming, DSA, OS, DBMS
- AI & ML → ML, models, datasets, regression, deep learning
- Mechanical → thermodynamics, machines, mechanics
- Civil → structures, materials
- Medical → anatomy, biology, clinical concepts

OUTPUT ONLY VALID JSON:

[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "correct_answer_index": 0,
    "topic": "specific topic"
  }}
]
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()

        data = json.loads(text)

        if not isinstance(data, list) or len(data) != 5:
            raise ValueError("Invalid response format")

        return data

    except Exception as e:
        print("❌ Error:", e)

        # fallback
        return [
            {
                "question": f"Basic concept in {specialization}",
                "options": ["A", "B", "C", "D"],
                "correct_answer_index": 0,
                "topic": specialization
            }
            for _ in range(5)
        ]


# Debug helper
def list_models():
    models = client.models.list()
    for m in models:
        print(m.name)