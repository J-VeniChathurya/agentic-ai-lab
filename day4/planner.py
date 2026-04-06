from groq import Groq
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

VALID_TOOLS = ["calculator", "average", "time", "summarizer", "weather"]

def clean_tools(tools):
    cleaned = []

    for t in tools:
        t = t.lower().strip()

        if "calc" in t or "sum" in t or "add" in t:
            cleaned.append("calculator")
        elif "time" in t:
            cleaned.append("time")
        elif "avg" in t:
            cleaned.append("average")
        elif "summ" in t:
            cleaned.append("summarizer")
        elif "weather" in t:
            cleaned.append("weather")

    return list(dict.fromkeys(cleaned))  # preserve order


def generate_plan(user_input):

    prompt = f"""
You are an AI planner.

Available tools:
calculator, average, time, summarizer, weather

Return ONLY a JSON array.

Example:
["calculator", "weather", "time"]

User: {user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()
    print("DEBUG RAW OUTPUT:", raw_output)

    # Try direct JSON
    try:
        return clean_tools(json.loads(raw_output))
    except:
        pass

    # Extract JSON manually
    match = re.search(r'\[.*?\]', raw_output)
    if match:
        try:
            return clean_tools(json.loads(match.group()))
        except:
            pass

    # 🔥 Fallback (VERY IMPORTANT)
    fallback = []
    text = user_input.lower()

    if any(word in text for word in ["sum", "add", "calculate", "+", "*", "-", "/"]):
        fallback.append("calculator")

    if "average" in text:
        fallback.append("average")

    if "time" in text:
        fallback.append("time")

    if "weather" in text:
        fallback.append("weather")

    if "summarize" in text:
        fallback.append("summarizer")

    return fallback