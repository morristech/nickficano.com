# -*- coding: utf-8 -*-
from __future__ import absolute_import
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from nickficano import frontend, api

application = DispatcherMiddleware(frontend.create_app(), {
    '/apis': api.create_app()
})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True,
               use_debugger=True)
