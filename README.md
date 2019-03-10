# Brood War Twitter Initiative

A site to help people get hooked up on twitter with various Brood War personalities.

## Set up dev environment
1) Install Python (3.7 is what this was built on, caveat emptor or something https://www.python.org/downloads/)
2) Get Django 2.1.7 `pip install Django==2.1.7`
3) Clone the Twython fork (https://github.com/vaidashwin/twython) (TODO update this with Twython master if oembed fixes are merged)
4) `cd` into Twython clone and run `python setup.py install`
5) `cd` into `bwtwitter/bwti` and run `python manage.py makemigrations`
6) Run `python manage.py sqlmigrate follow 0001`
7) Run `python manage.py migrate`
8) Everything should be good, run `python manage.py runserver` to start it up and hit it on `localhost:8000/follow`
