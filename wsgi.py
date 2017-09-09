from __future__ import absolute_import

from werkzeug.wsgi import DispatcherMiddleware

from nickficano import api
from nickficano import frontend

# This is the entry point for callable or entry point function for uwsgi.
application = DispatcherMiddleware(
    frontend.create_app(), {
        '/apis': api.create_app(),
    },
)
