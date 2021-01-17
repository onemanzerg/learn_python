from flask import Flask, jsonify
import time

APP_NAME = 'messenger'

app = Flask(APP_NAME)

@app.route('/')
def index():
    return APP_NAME

@app.route('/status')
def status():
    msg = {
        'status': True,
        'name': APP_NAME,
        'time': time.time()
    }

    return jsonify(msg)

if __name__ == "__main__":
    app.run()