# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template as T
from . import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    return T('index.j2')
