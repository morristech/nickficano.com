# -*- coding: utf-8 -*-
from __future__ import absolute_import
from contextlib import contextmanager
from fabric.api import cd, env, prefix, put, run, sudo, local

env.hosts = ['nickficano.com']
# Use authentication information stored in `~/.ssh/config`.
env.use_ssh_config = True
# TODO: Replace hardcoded paths with setting variables.


@contextmanager
def virtualenv(name):
    """Handy context manager to activate a virtualenv."""
    with prefix('WORKON_HOME=$HOME/.virtualenvs'):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            with prefix("workon {0}".format(name)):
                yield


def deploy():
    """Deploy updates to production."""
    git_pull()
    update_overrides()
    pip_update()
    restart_uwsgi()


def deploy_diglet():
    """Pull the latest version of the gendo codebase."""
    with cd('~/diglet/'):
        sudo('git pull origin master', user='ubuntu')

    with virtualenv("diglet"):
        with cd('~/diglet/'):
            run("pip install --ignore-installed -r requirements.txt")
    sudo("supervisorctl restart digletbot")


def deploy_sc():
    """Pull the latest version of the gendo codebase."""
    with cd('~/simplecontactsbot/'):
        sudo('git pull origin master', user='ubuntu')

    with virtualenv("simplecontactsbot"):
        with cd('~/simplecontactsbot/'):
            run("pip install --ignore-installed -r requirements.txt")
    sudo("supervisorctl restart simplecontactsbot")


def git_pull():
    """Pull the latest version of the codebase."""
    with cd('~/nickficano.com/app'):
        sudo('git pull origin master', user='www-data')


def restart_uwsgi():
    """Gracefully restart uwsgi."""
    sudo("supervisorctl restart www_uwsgi")


def pip_update():
    """Ensure all pip dependencies are up-to-date (or at least sync w/
    `requirements.txt`).
    """
    with virtualenv("nickficano.com"):
        with cd('~/nickficano.com/app'):
            run("pip install --ignore-installed -r requirements.txt")


def update_overrides():
    """Copies overrides.py to remote host."""
    with cd('/tmp'):
        put('nickficano/overrides.py', 'overrides.py')
        sudo('chown www-data:www-data overrides.py')
        sudo('mv overrides.py ~/nickficano.com/app/nickficano',
            user='www-data')


def regenerate_ssl_certs():
    local("openssl genrsa 4096 > account.key")
    local("openssl genrsa 4096 > domain.key")
