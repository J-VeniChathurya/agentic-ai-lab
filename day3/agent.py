from tools import execute_tool
from llm import decide_tool
from logger import log_interaction

EXIT_COMMANDS = ["exit", "end", "quit"]

def run_agent():
    print("LLM-Based Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input in EXIT_COMMANDS:
            print("Goodbye!")
            break

        tool = decide_tool(user_input)
        result = execute_tool(tool, user_input)

        print(result)

        # log everything
        log_interaction(user_input, tool, result)


if __name__ == "__main__":
    run_agent()