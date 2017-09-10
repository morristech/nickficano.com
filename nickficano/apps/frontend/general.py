from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask import send_from_directory

from nickficano.routing import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    return render_template('index.j2')


@route(bp, '/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')


@route(bp, '/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')
