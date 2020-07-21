from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote

@main.route('/')
def index():
    quote = get_quote()
    return render_template('index.html',quote=quote)
