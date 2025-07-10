import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run_shell():
    cmd = request.args.get('cmd')
    os.system(cmd)         # insecure: shell injection
    return "Executed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
