from asyncio.windows_events import NULL
from ipaddress import ip_address
from itertools import count
from operator import methodcaller
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import Model, SQLAlchemy
#libraries for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_manager, login_required, login_user, logout_user
import datetime
import counttry

app = Flask(__name__)
#initialisation of sqlalchemy
db = SQLAlchemy()

########################################################################
#setting all the configuration keys
app.config['SECRET_KEY'] = 'chakka is a very good fruit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
########################################################################
db.init_app(app)
class User(UserMixin, db.Model):  #The UserMixin will add Flask-Login attributes to the model so that Flask-Login will be able to work with it.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
class IPADDRESS(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    IPaddress = db.Column(db.String(100))
    #sqlite does not have the provision to store date and time, so we use string for it
    dandt = db.Column(db.String(100))
class Visitors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    count = db.Column(db.Integer)
    def __init__(self):
        self.count = 0
with app.app_context():
    db.create_all()

#getting the user logged in info
login_manager = LoginManager()
login_manager.login_view='login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route("/login")
def login():
    try:
        p = current_user.username
        flash("Already logged in!")
        return redirect(url_for('admin'))
    except:
        return render_template("adminLogin.html")

@app.route("/loginv", methods=['POST'])
def loginv():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = False  #can be used in the future to include the remember me functionality
    print(username, password)
    fetch_user = User.query.filter_by(username=username).first()
    if not fetch_user or not check_password_hash(fetch_user.password, password):
        flash("Please check your login credentials and try again!")
        return redirect(url_for('login'))
    #to log the ip address and , date and time of logging in as admin
    currentDateTime = datetime.datetime.now()
    new_ip = IPADDRESS(IPaddress = request.remote_addr, dandt = currentDateTime)
    db.session.add(new_ip)
    db.session.commit()
    #to increment the number of visitors
    v = Visitors.query.first()
    if not v:
        v = Visitors()
        v.count += 1
        db.session.add(v)
    v.count += 1
    db.session.commit()
    login_user(fetch_user, remember=remember)
    return redirect(url_for('admin'))

@app.route("/admin-signup")
def adsign():
    return render_template("signin.html", flag = 0)

#route for accepting the new admin sign in requests
@app.route("/createadmin", methods=['POST'])
def createadmin():
    username = request.form.get("username")
    password = request.form.get("pass")
    print(username, password)
    user = User.query.filter_by(username = username).first()
    if user:
        flash("Admin with that particular position already exists")
        return redirect(url_for('adsign'))
    else:
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
def home():
    v = Visitors.query.first()
    v.count += 1
    db.session.add(v)
    db.session.commit()
    return render_template("main.html", visitor = v.count)

@app.route("/admin")
@login_required
def admin():
    v = Visitors.query.first().count
    return render_template("main.html", name = current_user.username, visitor = v)


if __name__ == "__main__":
    app.run(debug=True)
"""
export FLASK_APP=project
export FLASK_DEBUG=1
"""