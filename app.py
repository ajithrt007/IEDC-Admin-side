from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#initialisation of sqlalchemy
db = SQLAlchemy()

########################################################################
#setting all the configuration keys
app.config['SECRET_KEY'] = 'chakka is a very good fruit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
########################################################################
db.init_app(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
with app.app_context():
    db.create_all()

@app.route("/login")
def login():
    return render_template("adminLogin.html")

@app.route("/admin-signup")
def adsign():
    return render_template("signin.html", flag = 1)

@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
"""
export FLASK_APP=project
export FLASK_DEBUG=1
"""