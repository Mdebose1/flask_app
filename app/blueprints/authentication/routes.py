from flask import current_app as app, render_template

@app.route('/signup')
def sign_up():
    return 'Sign-up'    