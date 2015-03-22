# -*- coding: utf-8 -*-
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from nickficano import frontend

application = DispatcherMiddleware(frontend.create_app())

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=False,
               use_debugger=False)
