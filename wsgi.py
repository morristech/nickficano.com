# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware

from nickficano import frontend

app = DispatcherMiddleware(frontend.create_app())
