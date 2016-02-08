# -*- coding: utf-8 -*-
from __future__ import absolute_import
from werkzeug.wsgi import DispatcherMiddleware
from nickficano import frontend, api

# This is the entry point for callable or entry point function for uwsgi. See:
# http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html#deploying-flask
application = DispatcherMiddleware(frontend.create_app(), {
    '/apis': api.create_app()
})
