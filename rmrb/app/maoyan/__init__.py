from flask import Blueprint

maoyan = Blueprint('Maoyan', __name__)

from . import views
