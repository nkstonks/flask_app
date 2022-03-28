# Got this web app working on heroku by specifying the port waitress should run on.
# Did this by running the script with a port argument (see procfile) 
import re
from flask import Flask, render_template, request, url_for, redirect, session
import os
import pymongo
import bcrypt
import admincreds
import emailer
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://nkstonks:Kento0303@logins.cs2j1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
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
    explanation = "This bit is still in the works."
    return render_template("about.html", explanation=explanation)

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
        auth_tuple = (str(form.username.data), str(form.password.data))

        if auth_tuple in admincreds.credentials:
            if auth_tuple == admincreds.credentials[0]:
                message = "Hello there, welcome to the cooler kids club"
            else:
                message = None
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