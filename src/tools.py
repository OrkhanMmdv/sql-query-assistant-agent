from src.database import create_connection

def generate_sql(user_request):
    request = user_request.lower()

    if "older than 18" in request:
        return "SELECT * FROM students WHERE age > 18;"

    if "grade higher than 8" in request or "grade > 8" in request:
        return "SELECT * FROM students WHERE grade > 8;"

    if "from riga" in request:
        return "SELECT * FROM students WHERE city = 'Riga';"

    if "from baku" in request:
        return "SELECT * FROM students WHERE city = 'Baku';"

    if "all students" in request:
        return "SELECT * FROM students;"

    return None


def validate_sql(query):
    if query is None:
        return False

    blocked_words = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
    upper_query = query.upper()

    for word in blocked_words:
        if word in upper_query:
            return False

    return upper_query.strip().startswith("SELECT")


def execute_sql(query):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    connection.close()
    return rows


def format_results(rows):
    if not rows:
        return "No results found."

    result = []

    for row in rows:
        result.append(
            f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, City: {row[4]}"
        )

    return "\n".join(result)