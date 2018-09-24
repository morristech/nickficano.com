"""
nickficano.apps.frontend
------------------------

Frontend application instance using Flask's factory pattern.
"""
import os
from typing import Optional

from flask import render_template

from server import factory
from server.lib.manifest import get_webpack_manifest


def create_app(settings_override: Optional[object] = None):
    """Returns the frontend application instance"""
    cwd = os.path.dirname(os.path.abspath(__file__))
    package_path = [cwd]

    app = factory.create_app(
        __name__,
        package_path,
        settings_override,
    )
    setup_jinja_env(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app


def setup_jinja_env(app):
    app.jinja_env.globals['manifest'] = get_webpack_manifest()

def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code
