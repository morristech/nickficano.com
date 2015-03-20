# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template as tpl
from . import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    return tpl('index.j2')
