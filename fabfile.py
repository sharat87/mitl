from __future__ import print_function

from fabric.api import task, env, local, run, cd, lcd, put

env.hosts = ['sharat87@sharat87.webfactional.com']

@task(default=True)
def up():
    tempdir = '/tmp/mit-license'
    archive = 'mit-license.tar.bz2'

    local('cp -r . ' + tempdir)

    with lcd(tempdir):
        local('rm -v fabfile.py*')
        local('tar -cjf /tmp/' + archive + ' *')

    put('/tmp/' + archive)

    with cd('~/webapps/mit_license'):
        run('rm -rf ./*')
        run('tar -xjf ~/' + archive)
        run('rm ~/' + archive)

    local('rm -rf ' + tempdir + ' /tmp/' + archive)
