
import subprocess

def run_command():
    command = input("Enter a shell command: ")
    subprocess.call(command, shell=True)

run_command()
