from datetime import datetime

def perform_action(intent, user_input):
    
    if intent == "calculate":
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation"

    elif intent == "date":
        return f"Current Date: {datetime.now().date()}"

    elif intent == "greet":
        return "Hello! How can I help you?"

    else:
        return "Sorry, I don't understand that command."