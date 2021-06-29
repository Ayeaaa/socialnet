from flask import Blueprint

force = Blueprint('Force', __name__)

from . import views
