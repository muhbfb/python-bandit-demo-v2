
import subprocess
import shlex

def run_command():
    command = input("Enter a shell command: ")
    subprocess.call(shlex.split(command))

run_command()
