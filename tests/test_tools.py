import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from tools import generate_sql, validate_sql, format_results
from validator import validate_user_input


def test_generate_sql_all_students():
    query = generate_sql("Show all students")

    assert query == "SELECT * FROM students;"


def test_generate_sql_older_than_19():
    query = generate_sql("Which students are older than 19?")

    assert query == "SELECT * FROM students WHERE age > 19;"


def test_generate_sql_riga_students():
    query = generate_sql("Which students live in Riga?")

    assert query == "SELECT * FROM students WHERE city = 'Riga';"


def test_validate_safe_sql():
    query = "SELECT * FROM students;"

    assert validate_sql(query) is True


def test_block_dangerous_sql():
    query = "DROP TABLE students;"

    assert validate_sql(query) is False


def test_empty_input_validation():
    assert validate_user_input("") is False


def test_valid_input_validation():
    assert validate_user_input("Show all students") is True


def test_format_empty_results():
    result = format_results([])

    assert result == "No results found."