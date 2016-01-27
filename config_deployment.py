from subprocess import call
import os

if __name__ == '__main__':

    base_dir = os.getcwd()

    call(['python3', 'manage.py', 'collectstatic'])
    call(['touch', base_dir + '/Thud/ThudLog.log'])
    call(['touch', base_dir + '/Thud/games.db'])