from __future__ import absolute_import
# -*- coding: utf-8 -*-
import pkgutil
import importlib
from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application
    found in all modules for the specified package.
    """

    rv = []
    # A bit more magic than I like, but who gives a turkey.
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv
