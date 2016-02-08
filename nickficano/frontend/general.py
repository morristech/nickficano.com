# -*- coding: utf-8 -*-
from flask import (render_template as T, current_app as app,
                   request, send_from_directory, Blueprint)
from . import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    return T('index.j2')


@route(bp, '/robots.txt')
def robots():
    return send_from_directory(app.static_folder, request.path[1:])


@route(bp, '/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, request.path[1:])
