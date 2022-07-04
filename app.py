# Got this web app working on heroku by specifying the port waitress should run on.
# Did this by running the script with a port argument (see procfile) 
import re
from flask import Flask, render_template, request, url_for, redirect, session
import os
import pymongo
import bcrypt
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

password = os.environ.get("FLASK_APP_PSW")

client = pymongo.MongoClient(f"mongodb+srv://nkstonks:{password}@logins.cs2j1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["credentials"]
collection = mydb["credentials"]

class AdminForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

@app.route('/')
def home():
    greeting = 'Hello World'
    return render_template("home.html", greeting=greeting)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    situation = "The blog is being set up, please wait..."
    return render_template("blog.html", situation=situation)

@app.route('/hello')
def hello():
    return render_template("hello.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminForm()

    if form.validate_on_submit():
        # for debugging
        # thing = 'Login requested for user {}, remember_me={}'.format(form.username.data, form.password.data)
        # print(thing)

        username_corect = collection.find_one({"username" : form.username.data})
        password_correct = collection.find_one({"password" : form.password.data})

        if username_corect and password_correct:
            message = "Hello there, welcome to the cooler kids club"
            return render_template("secret_page.html", message=message)

        else:
            return render_template("login.html", title="admin sign in", form=form, invalid="Login details invalid")
    return render_template("admin.html", title="admin sign in", form=form)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    form = AdminForm()
    if "username" in session:
        session.pop("email", None)
        return render_template("logout.html")
    else:
        return render_template('login.html', form=form, invalid="Wtf you are already logged out. Did you mean to log in?")

# @app.route('/testing')
# def testing():
    # this path is for testing purposes
    # return render_template("status.html")

app.secret_key = 'BLAyu#7bcic234yrhnd/nq!@2t5fvk;qcwmwxd;232'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)