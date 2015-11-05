# -*- coding: utf-8 -*-
from __future__ import absolute_import
from contextlib import contextmanager
from fabric.api import cd
from fabric.api import env
from fabric.api import prefix
from fabric.api import put
from fabric.api import run
from fabric.api import sudo

env.hosts = ['nickficano.com']
# Use authentication information stored in `~/.ssh/config`.
env.use_ssh_config = True
# TODO: Replace hardcoded paths with setting variables.


@contextmanager
def virtualenv(name):
    """Handy context manager to activate a virtualenv.
    """
    with prefix('WORKON_HOME=$HOME/.virtualenvs'):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            with prefix("workon {}".format(name)):
                yield


def deploy():
    """Deploy updates to "production".
    """
    git_pull()
    update_overrides()
    pip_update()
    restart_uwsgi()


def deploy_gendo():
    """Pull the latest version of the gendo codebase.
    """
    with cd('~/gendo/'):
        sudo('git pull origin master', user='ubuntu')
    sudo("supervisorctl restart gendobot")


def git_pull():
    """Pull the latest version of the codebase.
    """
    with cd('~/nickficano.com/app'):
        sudo('git pull origin master', user='www-data')


def restart_uwsgi():
    """Gracefully restart uwsgi.
    """
    sudo("supervisorctl restart www_uwsgi")


def pip_update():
    """Ensure all pip dependencies are up-to-date (or at least sync w/
    `requirements.txt`).
    """
    with virtualenv("nickficano.com"):
        with cd('~/nickficano.com/app'):
            run("pip install --ignore-installed -r requirements.txt")


def update_overrides():
    """Copies overrides.py to remote host.
    """
    with cd('/tmp'):
        put('nickficano/overrides.py', 'overrides.py')
        sudo('chown www-data:www-data overrides.py')
        sudo('mv overrides.py ~/nickficano.com/app/nickficano',
             user='www-data')
