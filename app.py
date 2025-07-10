import shlex, subprocess

@app.route('/run')
def run_shell_safe():
    cmd = request.args.get('cmd')
    args = shlex.split(cmd)
    subprocess.run(args, check=True)
    return "Executed safely"
