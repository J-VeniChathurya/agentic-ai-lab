def identify_tool(user_input):
    
    if "calculate" in user_input:
        return "calculator"
    
    elif "weather" in user_input:
        return "weather"
    
    elif "summarize" in user_input:
        return "summarizer"
    
    elif "time" in user_input:
        return "time"
    
    else:
        return "unknown"