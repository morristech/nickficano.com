from __future__ import absolute_import

from flask_assets import Bundle
from flask_assets import Environment

css_all = Bundle(
    'scss/all.scss',
    depends=['**/*.scss'],
    filters='pyscss,cssmin',
    output='css/%(version)s/all.css',
)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.debug = app.debug
    webassets.auto_rebuild = app.debug
