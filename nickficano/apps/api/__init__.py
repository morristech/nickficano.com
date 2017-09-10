import os
from functools import wraps

from flask import jsonify

from nickficano import factory
from nickficano.lib.serializers import JSONEncoder


def create_app(settings_override=None):
    """Returns the API application instance"""
    path = [os.path.dirname(os.path.abspath(__file__))]
    app = factory.create_app(__name__, path, settings_override)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    app.errorhandler(404)(on_404)

    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator


def on_error(e):
    return jsonify(dict(error=e.msg)), 400


def on_404(e):
    return jsonify(dict(error='Not found')), 404
