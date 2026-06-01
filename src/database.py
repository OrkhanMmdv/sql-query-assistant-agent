import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "students.db"


def create_connection():
    # Ensure the database directory exists. The .db file itself is excluded
    # from Git (see .gitignore), so on a fresh clone this folder may not be
    # present yet. Creating it here lets the program run without manual setup.
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def setup_database():

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade REAL NOT NULL,
            city TEXT NOT NULL
        )
    """)

    cursor.execute("DELETE FROM students")

    students = [
        ("Orkhan", 20, 9.7, "Riga"),
        ("Kamal", 21, 9.2, "Riga"),
        ("Ali", 18, 7.5, "Baku"),
        ("Leyla", 22, 9.5, "Baku"),
        ("Nigar", 19, 6.8, "Ganja")
    ]

    cursor.executemany(
        "INSERT INTO students (name, age, grade, city) VALUES (?, ?, ?, ?)",
        students
    )

    connection.commit()
    connection.close()