def identify_intent(user_input):
    if "calculate" in user_input:
        return "calculate"
    elif "date" in user_input:
        return "date"
    elif "hello" in user_input or "hi" in user_input:
        return "greet"
    else:
        return "unknown"