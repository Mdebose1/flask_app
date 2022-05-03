from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('main/index.html')

@app.route('/contact')
def contact():
    return 'Contact'

@app.route('/about')
def about():
    return 'About'



