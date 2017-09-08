# -*- coding: utf-8 -*-
from __future__ import absolute_import

import click
from werkzeug.serving import run_simple

from wsgi import application as app


@click.group()
def cli():
    pass


@click.command()
@click.option('--port', default=5000, help='The port for the server.')
@click.option(
    '--hostname', default='localhost', help=(
        "The host for the application. eg: 'localhost'"
    ),
)
def runserver(hostname, port):
    run_simple(hostname, port, app, use_reloader=True, use_debugger=True)


if __name__ == '__main__':
    cli.add_command(runserver)
    cli()
