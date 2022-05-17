from flask import Blueprint

bp = Blueprint('authentication', __name__, template_folder='signup', url_prefix='/')

from .import routes