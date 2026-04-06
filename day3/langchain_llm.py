from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Use Groq model via LangChain
llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template("""
You are an AI agent.

Available tools:
calculator, weather, summarizer, time

Return ONLY one word (tool name).

User: {input}
""")

chain = prompt | llm

def decide_tool(user_input):
    response = chain.invoke({"input": user_input})

    tool = response.content.strip().lower()

    # 🔥 Clean output (important)
    tool = tool.split()[0]

    return tool