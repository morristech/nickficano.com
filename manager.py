from __future__ import absolute_import
# -*- coding: utf-8 -*-
from flask.ext.script import Server
from flask.ext.script import Manager
from nickficano.frontend import create_app

manager = Manager(create_app())
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == "__main__":
    manager.run()
