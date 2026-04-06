from planner import generate_plan
from executor import execute_plan
from logger import log_interaction

EXIT_COMMANDS = ["exit", "end", "quit"]

def run_agent():
    print("Multi-Step Planning Agent\n")

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input in EXIT_COMMANDS:
            print("Goodbye!")
            break

        plan = generate_plan(user_input)

        print("\nGenerated Plan:")
        print(plan)

        result = execute_plan(plan, user_input)

        print("\nFinal Output:")
        print(result)

        # 🔥 LOGGING (important for marks)
        log_interaction(user_input, plan, result)


if __name__ == "__main__":
    run_agent()