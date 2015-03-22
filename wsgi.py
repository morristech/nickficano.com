# -*- coding: utf-8 -*-
from werkzeug.wsgi import DispatcherMiddleware

from nickficano import frontend

app = DispatcherMiddleware(frontend.create_app())

if __name__ == '__main__':
    app.app.run(host='0.0.0.0')
