from flask import Flask, redirect, render_template, request
import cgi
import os



app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('sign.html')

@app.route("/sign-up", methods=['POST'])
def user_sign():
    username=request.form['user-name']
    email=request.form['user-email']
    email = ['needs @ . no space']
    password_error=''
    password1 = request.form['pwd1']
    password2 = request.form['pwd2']
    if password1 != password2:
        password_error ='Passwords must match.'

    if not password_error:
        return render_template('welcome.html',username=username)
    else:
        email=email
        username=username
        return render_template('sign.html',password_error=password_error, username=username, email=email)

app.run()
