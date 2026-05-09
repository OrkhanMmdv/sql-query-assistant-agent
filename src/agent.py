from tools import (
    generate_sql,
    validate_sql,
    execute_sql,
    format_results
)

from validator import validate_user_input
from ai_sql_generator import generate_sql_with_ai


class SQLQueryAssistantAgent:

    def process_request(self, user_request):

        if not validate_user_input(user_request):
            return "Invalid input. Please enter a valid request."

        try:
            sql_query = generate_sql_with_ai(user_request)
            print(f"\nGenerated SQL: {sql_query}")

        except Exception as error:
            print(f"\nAI error: {error}")
            print("Using fallback rule-based generator.")
            sql_query = generate_sql(user_request)

        if sql_query is None:
            return "Sorry, I cannot understand this request yet."

        if not validate_sql(sql_query):
            return "Generated SQL query is not safe."

        rows = execute_sql(sql_query)

        return format_results(rows)