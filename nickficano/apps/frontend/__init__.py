"""
nickficano.apps.frontend
------------------------

Frontend application instance using Flask's factory pattern.
"""
import os

from typing import Optional
from flask import render_template

from nickficano.apps.frontend import assets
from nickficano import factory


def create_app(settings_override: Optional[object] = None):
    """Returns the frontend application instance"""
    path = [os.path.dirname(os.path.abspath(__file__))]
    app = factory.create_app(__name__, path, settings_override)

    # Init assets
    assets.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code
