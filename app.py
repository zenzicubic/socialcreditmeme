from flask import Flask, request, send_from_directory, redirect, render_template, Markup
import os
import json
from flask_cors import CORS

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))
c = CORS(app)
questions = [["nothing", "[REDACTED]", 0, "What happened in tiananmen square in 1989?"], ["Joe Biden", "Xi Jinping", 1, "Who is the best?"], ["Supreme Leader's clay, "Based independent territory", 0, "What is this? #taiwan-china.png#"], ["Indoctrination", "Playtime with Supreme Leader", 1, "What is happening here? #uighurs.png#"], ["None, because I work at factory all day", "All of them", 0, "How many hours did you spent gaming?"]]
results = [15, 150, 1500, 15000, 150000]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/question")
def question():
    i=int(request.args["index"])
    return json.dumps([results[i], questions[i]])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
