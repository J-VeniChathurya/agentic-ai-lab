from input_handler import get_user_input
from decision import identify_tool
from tools import execute_tool

EXIT_COMMANDS = ["exit", "end", "quit"]

def run_agent():
    print("Tool-Using Agent (type 'exit' to quit)\n")

    while True:
        user_input = get_user_input()

        if user_input in EXIT_COMMANDS:
            print("Goodbye!")
            break

        tool = identify_tool(user_input)
        result = execute_tool(tool, user_input)

        print(result)


if __name__ == "__main__":
    run_agent()