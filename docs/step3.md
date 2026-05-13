# Step 3 – Testing and Deployment Preparation

## Testing Process

Testing was performed during implementation. Each main component was tested separately and then the full workflow was tested through the command-line interface.

The testing process included SQL generation, SQL validation, database execution, input validation, result formatting, AI integration, and fallback behavior.

## Test Scenarios

1. Show all students  
Expected result: all student records are returned.

2. Which students are older than 19?  
Expected result: only students with age greater than 19 are returned.

3. Which students live in Riga?  
Expected result: only students from Riga are returned.

4. Empty input  
Expected result: the system returns an invalid input message.

5. Dangerous SQL command  
Expected result: commands such as DROP, DELETE, UPDATE, INSERT, and ALTER are blocked.

6. Gemini API failure or quota limit  
Expected result: the system switches to the fallback rule-based SQL generator.

## Deployment Preparation

The project is prepared as a local command-line Python application. Another user can clone the repository, install dependencies, create a `.env` file with a Gemini API key, and run the program.

Run the system:

```bash
pip install -r requirements.txt
python src/main.py