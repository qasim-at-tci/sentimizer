from flask import Flask, jsonify, request
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)


@app.route("/uptime")
def uptime():
    return jsonify({"status": "OK"})


@app.route("/api/v1/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")
    tblob = TextBlob(text)
    res = jsonify(
        {
            "input": {"text": text},
            "sentiment": {
                "polarity": tblob.sentiment.polarity,
                "subjectivity": tblob.sentiment.subjectivity,
            },
        }
    )
    res.status_code = 200
    return res
