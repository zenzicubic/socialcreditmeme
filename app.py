from flask import Flask, request, send_from_directory, redirect, render_template, Markup
import os
from flask_cors import CORS

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))
c = CORS(app)
questions = [{"What happened in tiananmen square in 1989?" : ["nothing", "[REDACTED]", 0]}, {"Who is the best?" : ["Joe Biden", "Xi Jinping", 1]}, {"What is this? <img src=\"/static/taiwan.png\">" : ["Glorious Leader's concrete slab", "Based independent territory", 0]}, {"What is happening here? <img src=\"uighurs.png\">" : ["Indoctrination", "Playtime with Great Leader", 1]}, {"How many hours did you spent gaming?" : ["None, because I work at factory all day", "All of them", 0]}]
results = [15, 150, 1500, 15000, 150000]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/question", methods=["GET", "POST"])
def question():
    no = request.form.get("no")
    score = request.form.get("score")
    key=list(questions[int(no-1)].keys)[0]
    return render_template("q.html", head=key, a1=questions[no][key][0], a2=questions[no][key][1], score=score, no=no)

@app.route("/result", methods=["GET", "POST"])
def result():
    no = int(request.form.get("no"))
    score = int(request.form.get("score"))
    ans = int(request.form.get("ans"))
    cans=list(questions[no-1].values)[3]
    if (no < 4):
        if (ans==cans):
            score += results[no]
        else:
            score -= results[no]
        return render_template("a.html", im=str(results[no])+".png", score=str(score+amount), no=str(no+1))
    else:
        if (score == 166665):
            return ""
        else:
            return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
