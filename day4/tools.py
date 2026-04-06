import requests
import os
from dotenv import load_dotenv
import re

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
        text = user_input.lower()

        replacements = {
            "plus": "+",
            "add": "+",
            "sum": "+",
            "minus": "-",
            "subtract": "-",
            "multiply": "*",
            "multiplied by": "*",
            "times": "*",
            "divide": "/",
            "divided by": "/"
        }

        for word, symbol in replacements.items():
            text = text.replace(word, symbol)

        # 🔥 FIX: convert "2 and 3" → "2+3"
        match = re.search(r'(\d+)\s*and\s*(\d+)', text)
        if match:
            text = f"{match.group(1)}+{match.group(2)}"

        expression = re.findall(r"[0-9+\-*/().]+", text)
        expression = "".join(expression)

        if not expression:
            return "No valid expression found"

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

        text = user_input.lower()

        # 🔥 extract city after "in"
        if "in" in text:
            city = text.split("in")[-1].strip().split()[0]
        else:
            city = "mumbai"  # fallback

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            return "Weather error"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"Weather in {city.title()}: {temp}°C, {desc}"

    except:
        return "Weather fetch failed"




# 🔹 Summarizer Tool (Simple logic)
def summarizer_tool(user_input):
    try:
        text = user_input.replace("summarize", "").strip()
        
        sentences = text.split(".")
        summary = sentences[0]  # basic summary
        
        return f"Summary: {summary.strip()}"
    except:
        return "Could not summarize"

def average_tool(numbers):
    if not numbers:
        return "No numbers provided"
    
    avg = sum(numbers) / len(numbers)
    return avg


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