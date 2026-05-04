from database import setup_database
from agent import SQLQueryAssistantAgent


def main():
    setup_database()

    agent = SQLQueryAssistantAgent()

    print("SQL Query Assistant Agent")
    print("Example: Show all students with grade higher than 8")
    print("Type 'exit' to stop.")

    while True:
        user_request = input("\nEnter your request: ")

        if user_request.lower() == "exit":
            print("Goodbye!")
            break

        response = agent.process_request(user_request)

        print("\nResult:")
        print(response)


if __name__ == "__main__":
    main()