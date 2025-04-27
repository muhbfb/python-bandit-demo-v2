import subprocess  # nosec

def run_command():
    allowed_commands = {
        "list": ["ls", "-la"],
        "date": ["date"],
        "uptime": ["uptime"]
    }
    choice = input("Enter command (list/date/uptime): ")
    if choice in allowed_commands:
        subprocess.call(allowed_commands[choice])  # nosec
    else:
        print("Command not allowed.")

run_command()
