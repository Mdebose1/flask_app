from flask import render_template, current_app as app
from datetime import datetime as dt


@app.route('/')
def home():
    # raise Exception('This is a general exception I\'m trying to raise for no reason.')
    return render_template('main/index.html')

@app.route('/profile')
def profile():
    return render_template('main/profile.html')

@app.route('/contact')
def contact():
    return "Contact Page"


@app.route('/login')
def login():
    return 'Login'

@app.route('/register')
def register():
    return 'Register'

@app.route('/logout')
def logout():
    return 'Logout'





