from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

my_app = Flask(__name__)

@my_app.route("/emotionDetection")
def detect_emotion():
    text = requests.args.get("text_to_analyze")
    result = emotion_detector(text)
    return result

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)