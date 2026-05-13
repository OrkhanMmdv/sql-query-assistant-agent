# sql-query-assistant-agent

Python-based AI-assisted SQL Query Assistant Agent that converts natural language requests into SQL queries and executes them on a local SQLite database. The system demonstrates an AI/agent workflow with Gemini API integration, SQL validation, database execution, result formatting, testing, and deployment preparation.

---

# Features

* Natural language to SQL conversion
* Gemini AI integration
* SQLite database support
* SQL query validation
* Result formatting
* Input validation
* Fallback rule-based SQL generator
* Automated testing with pytest
* Modular Python project structure

---

# Technologies Used

* Python
* SQLite3
* Gemini API
* python-dotenv
* pytest
* Git & GitHub

---

# Project Structure

```bash
sql-query-assistant-agent/
│
├── src/
│   ├── main.py
│   ├── agent.py
│   ├── ai_sql_generator.py
│   ├── database.py
│   ├── tools.py
│   └── validator.py
│
├── database/
│   └── students.db
│
├── tests/
│   └── test_tools.py
│
├── docs/
│   ├── step1.md
│   ├── step2.md
│   └── step3.md
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# How the System Works

```text
User Request
↓
Gemini AI generates SQL
↓
SQL validation tool checks query
↓
SQLite database executes query
↓
Result formatting tool prepares output
↓
Final result returned to user
```

If the AI service fails or quota is exceeded, the system automatically switches to the fallback rule-based SQL generator.

---

# Installation

Clone repository:

```bash
git clone YOUR_REPOSITORY_LINK
cd sql-query-assistant-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should not be uploaded to GitHub.

---

# Running the Program

Run:

```bash
python src/main.py
```

Example requests:

```text
Show all students
```

```text
Which students are older than 19?
```

```text
Which students live in Riga?
```

---

# Running Tests

Run:

```bash
python -m pytest
```

---

# Database Information

The system currently uses a local SQLite database:

```text
database/students.db
```

The database contains a sample `students` table with student information.

The system can be extended to support additional SQLite databases and dynamic schema analysis.

---

# Testing

The project includes:

* SQL generation testing
* SQL validation testing
* Input validation testing
* Result formatting testing
* Functional workflow testing
* AI fallback testing

---

# Deployment Strategy

The current version is prepared as a local command-line application for controlled testing and development.

Possible future deployment options:

* Web service
* API-based assistant
* Cloud database integration
* Multi-database support
* Containerized deployment

---

# Author

Developed as part of an AI-assisted software systems practical assignment.
