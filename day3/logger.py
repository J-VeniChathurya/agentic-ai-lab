def log_interaction(user_input, tool, output):
    with open("logs.txt", "a") as f:
        f.write(f"INPUT: {user_input}\n")
        f.write(f"TOOL: {tool}\n")
        f.write(f"OUTPUT: {output}\n")
        f.write("-" * 40 + "\n")