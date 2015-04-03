from __future__ import absolute_import
# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware
from nickficano import frontend

application = DispatcherMiddleware(frontend.create_app())
