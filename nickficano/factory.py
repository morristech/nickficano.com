from flask import Flask
from .helpers import register_blueprints


def create_app(package_name, package_path, settings_override=None):
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('nickficano.settings')
    app.config.from_object(settings_override)

    register_blueprints(app, package_name, package_path)

    return app
