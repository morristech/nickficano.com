# -*- coding: utf-8 -*-
from contextlib import contextmanager
from fabric.api import cd
from fabric.api import env
from fabric.api import prefix
from fabric.api import run
from fabric.api import sudo

env.hosts = ['nickficano.com']
# Use authentication information stored in `~/.ssh/config`.
env.use_ssh_config = True


@contextmanager
def virtualenv(name):
    with prefix("workon {}".format(name)):
        yield


def deploy():
    """Deploy updates to production.
    """
    git_pull()
    restart_uwsgi()


def git_pull():
  """Pull the latest version of the codebase.
  """
  with cd('~/nickficano.com/app'):
      sudo('git pull origin master', user='www-data')


def restart_uwsgi():
  """Gracefully restart uwsgi.
  """
  sudo("supervisorctl restart www_uwsgi")


def update_dependencies():
    """Ensure all pip dependencies are up-to-date.
    """
    with virtualenv("nickficano.com"):
        with cd('~/nickficano.com/app'):
            run("pip install --ignore-installed -r requirements.txt")
