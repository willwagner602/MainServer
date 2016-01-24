from subprocess import call
import os

if __name__ == '__main__':

    current_dir = os.getcwd()
    app_dirs = ['Thud', 'Thu2d', 'PyJobsDjango', 'LandingPage']

    for dir in app_dirs:
        os.chdir(dir)
        call(['git', 'pull'])
        os.chdir(current_dir)