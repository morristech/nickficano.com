from werkzeug.wsgi import DispatcherMiddleware

from nickficano.apps import api
from nickficano.apps import frontend

# This is the entry point for callable or entry point function for uwsgi.
application = DispatcherMiddleware(
    frontend.create_app(), {
        '/apis': api.create_app(),
    },
)
