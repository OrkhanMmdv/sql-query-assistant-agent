import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

# The client is created lazily (inside the function) instead of at import time.
# This way, if the GEMINI_API_KEY is missing or invalid, importing this module
# does NOT crash the whole program. The error is raised only when AI generation
# is actually attempted, so the agent can catch it and switch to the
# rule-based fallback generator.
_client = None


def get_client():
    global _client

    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not set.")

        _client = genai.Client(api_key=api_key)

    return _client


def clean_sql_output(text):

    sql = text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


def generate_sql_with_ai(user_request):

    client = get_client()

    prompt = f"""
    Convert the following user request into a safe SQLite SELECT query.

    Database table:
    students(id, name, age, grade, city)

    Rules:
    - Only generate SELECT queries
    - Do not generate DELETE, DROP, UPDATE, INSERT
    - Return only SQL query
    - Do not use markdown code blocks
    - SQLite syntax only

    User request:
    {user_request}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return clean_sql_output(response.text)
