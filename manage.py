import click
from werkzeug.serving import run_simple

from wsgi import application as app


@click.group()
def cli():
    pass


@click.command()
@click.option('--port', default=5000, help='The server port number')
@click.option('--hostname', default='localhost', help='The server hostname')
def runserver(hostname: str, port: int):
    run_simple(hostname, port, app, use_reloader=True, use_debugger=True)


if __name__ == '__main__':
    cli.add_command(runserver)
    cli()
