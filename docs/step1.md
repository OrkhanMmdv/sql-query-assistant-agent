# Step 1 – Project Planning

## System Goal

The planned system is an AI-assisted SQL Query Assistant Agent developed in Python. The goal of the system is to help computer science students and beginner database users interact with databases using natural language instead of writing SQL manually.

The system receives a text request such as “Which students are older than 19?” or “Show students from Riga”, converts it into an SQL query using Gemini AI, validates the generated query, executes it on a local SQLite database, and returns formatted database results containing student information.

## AI / Agent-Based Approach

The system uses an AI-assisted agent-based approach. Gemini AI converts natural language requests into SQL queries. The agent coordinates the workflow: user input, AI SQL generation, SQL validation, database execution, result formatting, and final output.

If the Gemini API fails or quota is exceeded, the system switches to a fallback rule-based SQL generator.

## Tools

The system uses Gemini API for SQL generation, SQLite for local database storage, SQL validation tools for safety, result formatting tools for readable output, and input validation tools to check user input.

## Programming Concepts

The project requires Python functions, classes, modules, conditional statements, string processing, SQLite integration, exception handling, user input/output, testing, Git, and GitHub.