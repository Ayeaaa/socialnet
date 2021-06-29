from flask import Blueprint

movie = Blueprint('Movie', __name__)

from . import views
