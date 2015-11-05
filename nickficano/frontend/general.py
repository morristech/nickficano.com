# -*- coding: utf-8 -*-
import os
from contextlib import contextmanager

from flask import Blueprint
from flask import render_template as T
from fabric.api import cd, run, sudo, prefix
from . import route

bp = Blueprint('index', __name__)


@route(bp, '/')
def index():
    pid = os.getpid()
    return T('index.j2', pid=pid)


@contextmanager
def virtualenv(name):
    """Handy context manager to activate a virtualenv.
    """
    with prefix('WORKON_HOME=$HOME/.virtualenvs'):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            with prefix("workon {}".format(name)):
                yield


@route(bp, '/webhooks/github/gendo/', methods=('GET', 'POST',))
def gendo_webhook():
    with cd('~/gendo/'):
        sudo('git pull origin master', user='ubuntu')

    with virtualenv("gendo"):
        with cd('~/gendo/'):
            run("pip install --ignore-installed -r requirements.txt")
    sudo("supervisorctl restart gendobot")
    return "OK"
