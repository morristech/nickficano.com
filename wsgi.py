# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware
from flask import Flask
from nickficano import frontend

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(frontend.create_app())
app.run(host="0.0.0.0")
