from input_handler import get_user_input
from decision import identify_intent
from actions import perform_action

def run_agent():
    print("Simple Rule-Based AI Agent (type 'exit' to quit)\n")
    
    while True:
        user_input = get_user_input()

        if user_input == "exit":
            print("Goodbye!")
            break

        intent = identify_intent(user_input)
        response = perform_action(intent, user_input)

        print(response)

if __name__ == "__main__":
    run_agent()