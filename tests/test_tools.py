from src.tools import generate_sql, validate_sql


def test_generate_sql():
    query = generate_sql("Show all students")

    assert query == "SELECT * FROM students;"


def test_validate_sql():
    valid_query = "SELECT * FROM students;"
    invalid_query = "DROP TABLE students;"

    assert validate_sql(valid_query) is True
    assert validate_sql(invalid_query) is False