# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware
from flask import Flask
from nickficano import frontend

application = Flask(__name__)
application.wsgi_app = DispatcherMiddleware(frontend.create_app())
application.run(host="0.0.0.0")
