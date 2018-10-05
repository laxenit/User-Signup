from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/sign-up", methods=['POST'])
def user_signup():
    username=request.form['user-name']
    email=request.form['user-email']
    password_error=''
    password1 = request.form['pwd1']
    password2 = request.form['pwd2']
    if password1 != password2:
        password_error ='Passwords must match.'

    if not password_error:
        return render_template('welcome_page.html',username=username)
    else:
        email=email
        username=username
        return render_template('signup.html',password_error=password_error, username=username, email=email)

app.run()