# -*- coding: utf-8 -*-
import os

from flask import Blueprint
from flask import render_template as T
from . import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    pid = os.getpid()
    return T('index.j2', pid=pid)
