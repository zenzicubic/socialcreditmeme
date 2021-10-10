from flask import Flask, request, send_from_directory, redirect, render_template, Markup
import os
from flask_cors import CORS

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))
c = CORS(app)

@app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
