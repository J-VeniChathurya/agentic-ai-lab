from datetime import datetime
import re

def handle_input(user_input):
    return user_input.lower()


def decision_logic(user_input):

    if "hello" in user_input:
        return "greeting"

    elif "date" in user_input:
        return "date"

    elif "calculate" in user_input:
        return "calculate"

    else:
        return "unknown"


def execute_action(intent, user_input):

    if intent == "greeting":
        return "Hello! How can I help you?"

    elif intent == "date":
        return datetime.now().strftime("%Y-%m-%d")

    elif intent == "calculate":

        numbers = re.findall(r'\d+', user_input)

        if len(numbers) >= 2:
            return int(numbers[0]) + int(numbers[1])
        else:
            return "Please provide two numbers."

    else:
        return "Sorry, I don't understand."


def agent():

    user_input = input("Enter command: ")

    processed = handle_input(user_input)

    intent = decision_logic(processed)

    result = execute_action(intent, processed)

    print("Agent:", result)


agent()