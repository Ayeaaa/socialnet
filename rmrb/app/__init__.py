from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/dataviz2021?charset=utf8'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    db.init_app(app)

    from .yien import yien as yien_blueprint
    app.register_blueprint(yien_blueprint, url_prefix='/')

    from .maoyan import maoyan as maoyan_blueprint
    app.register_blueprint(maoyan_blueprint, url_prefix='/')

    from .movie import movie as movie_blueprint
    app.register_blueprint(movie_blueprint, url_prefix='/')
    return app

