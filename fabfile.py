# -*- coding: utf-8 -*-
from fabric.api import cd
from fabric.api import env
from fabric.api import sudo

env.hosts = ['nickficano.com']
env.use_ssh_config = True


def deploy():
    git_pull()
    restart_uwsgi()


def git_pull():
  with cd('~/nickficano.com/app'):
      sudo('git pull origin master', user='www-data')


def restart_uwsgi():
  sudo("supervisorctl restart www_uwsgi")
