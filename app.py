from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/uptime")
def uptime():
    return jsonify({"status": "OK"})
