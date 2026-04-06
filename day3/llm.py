from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def decide_tool(user_input):

    prompt = f"""
You are an AI agent.

Available tools:
calculator, weather, summarizer, time

User input: "{user_input}"

Return ONLY one word (tool name).
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    tool = response.choices[0].message.content.strip().lower()
    return tool