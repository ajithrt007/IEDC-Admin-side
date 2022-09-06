from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("user.html")

@app.route("/events")
def events():
    return render_template("event-details.html")

@app.route("/game")
def game():
    return render_template("game.html")


if __name__ == "__main__":
    app.run(debug=True)