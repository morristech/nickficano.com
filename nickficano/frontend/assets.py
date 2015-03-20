# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle
from flask.ext.assets import Environment

css_all = Bundle("scss/all.scss", depends=["**/*.scss"], filters="pyscss",
                 output="css/all.css", debug=True)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.cache = not app.debug
    webassets.debug = app.debug
