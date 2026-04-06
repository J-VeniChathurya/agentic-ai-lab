import re
from tools import average_tool, summarizer_tool, time_tool, calculator_tool, weather_tool

def execute_plan(plan, user_input):

    print("\n--- Execution Steps ---")

    results = []

    for step in plan:

        if step == "calculator":
            result = calculator_tool(user_input)
            print(f"Calculation → {result}")
            results.append(result)

        elif step == "average":
            numbers = list(map(int, re.findall(r'\d+', user_input)))
            avg = average_tool(numbers)
            print(f"Average → {avg}")
            results.append(f"Average: {avg}")

        elif step == "weather":
            result = weather_tool(user_input)
            print(f"Weather → {result}")
            results.append(result)

        elif step == "time":
            result = time_tool(user_input)
            print(f"Time → {result}")
            results.append(result)

    # 🔥 IMPORTANT: summarizer should run LAST
    if "summarizer" in plan:
        combined_text = " ".join(results)
        summary = summarizer_tool("summarize " + combined_text)
        print(f"Summary → {summary}")
        results.append(summary)

    return "\n".join(results)