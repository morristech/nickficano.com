# -*- coding: utf-8 -*-
from fabric.api import cd
from fabric.api import env
from fabric.api import sudo

env.hosts = ['nickficano.com']
# Use authentication information stored in `~/.ssh/config`.
env.use_ssh_config = True


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
