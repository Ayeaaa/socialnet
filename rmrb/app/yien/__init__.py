from flask import Blueprint

yien = Blueprint('Yien', __name__)

from . import views
