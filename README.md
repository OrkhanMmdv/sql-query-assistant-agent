# sql-query-assistant-agent

Python-based SQL Query Assistant Agent that converts simple natural language requests into SQL queries and executes them on a local SQLite database. The system demonstrates an AI/agent workflow with tool usage, query validation, result formatting, testing, and deployment preparation.

## Features

* Natural language to SQL conversion
* SQLite database integration
* Query validation
* Result formatting
* Input validation
* Modular Python structure
* Functional testing

## Technologies Used

* Python
* SQLite3
* Git & GitHub
* Pytest

## Project Structure

```bash
sql-query-assistant-agent/
│
├── src/
├── database/
├── tests/
├── requirements.txt
├── README.md
└── report.md
```

## Example

User input:

```text
Show all students with grade higher than 8
```

Generated SQL:

```sql
SELECT * FROM students WHERE grade > 8;
```

## Planned Workflow

```text
User Request
↓
Agent Analysis
↓
SQL Generation Tool
↓
Query Validation
↓
Database Execution
↓
Formatted Result
```

## Status

Step 1 completed — project planning and system design.
