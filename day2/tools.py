import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

from datetime import datetime

# 🔹 Time Tool
def time_tool(user_input):
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Current Time: {current_time}"

# 🔹 Calculator Tool
def calculator_tool(user_input):
    try:
        expression = user_input.replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation"


def weather_tool(user_input):
    try:
        import requests
        import os
        from dotenv import load_dotenv

        load_dotenv()
        API_KEY = os.getenv("OPENWEATHER_API_KEY")
        

        # 🔥 Better city extraction
        user_input = user_input.lower()

        if "in" in user_input:
            city = user_input.split("in")[-1].strip()
        else:
            city = user_input.replace("weather", "").strip()

        # Capitalize properly
        city = city.title()

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        # Debug (IMPORTANT)
        # print(data)

        if str(data.get("cod")) != "200":
            return f"City not found: {city}"

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"Weather in {city}: {temp}°C, {description}"

    except Exception as e:
        return f"Error: {str(e)}"




# 🔹 Summarizer Tool (Simple logic)
def summarizer_tool(user_input):
    try:
        text = user_input.replace("summarize", "").strip()
        
        sentences = text.split(".")
        summary = sentences[0]  # basic summary
        
        return f"Summary: {summary.strip()}"
    except:
        return "Could not summarize"


# 🔹 Tool Dispatcher
def execute_tool(tool_name, user_input):
    
    if tool_name == "calculator":
        return calculator_tool(user_input)
    
    elif tool_name == "weather":
        return weather_tool(user_input)
    
    elif tool_name == "summarizer":
        return summarizer_tool(user_input)
    
    elif tool_name == "time":
        return time_tool(user_input)
    
    else:
        return "Tool not found"