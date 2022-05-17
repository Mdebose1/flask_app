from app import app


@app.errorhandler(404)
def not_found_error(error):
    return "There was an error with our servers."

@app.errorhandler(500)
def internal_server_error(error):
    return "There was an error with our servers. Please contact the system administrator."