from flask import Flask
from app.api.v1 import create_blue_print
from app.models.base import db

def create_blueprint(app: Flask):
    v1_pr = create_blue_print()
    app.register_blueprint(v1_pr, url_prefix='/v1')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')

    db.init_app(app)
    db.create_all(app=app)
    create_blueprint(app)
    return app