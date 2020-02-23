from flask import Blueprint
from app.api.v1 import book, user, client

def create_blue_print():
    v1_pr = Blueprint('v1', __name__)
    book.api.register(v1_pr, url_prefex='/book')
    user.api.register(v1_pr, url_prefex='/user')
    client.api.register(v1_pr, url_prefex='/client')
    return v1_pr