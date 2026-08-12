from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector
import json
from flask import render_template

my_app = Flask(__name__)

@my_app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response

@my_app.route("/")
def render_index_page():
    return render_template("index.html")
    

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
