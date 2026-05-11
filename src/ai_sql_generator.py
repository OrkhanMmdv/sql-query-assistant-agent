import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_sql_output(text):

    sql = text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


def generate_sql_with_ai(user_request):

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