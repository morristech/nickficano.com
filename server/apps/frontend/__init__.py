"""
nickficano.apps.frontend
------------------------

Frontend application instance using Flask's factory pattern.
"""
import os
from typing import Optional

from flask import render_template

from server import factory
from server.lib.static import get_raw_static_asset
from server.lib.static import get_webpack_manifest


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
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.add_extension('server.lib.jinja2_html_minifier.HTMLCompress')
    app.jinja_env.globals['manifest'] = get_webpack_manifest()
    app.jinja_env.globals['raw_static_asset'] = get_raw_static_asset


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code
