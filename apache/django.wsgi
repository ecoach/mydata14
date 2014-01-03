import os, sys

import site
site.addsitedir('/home/jtritz/virtualenv/v1/lib/python2.6/site-packages')

from os.path import abspath, dirname, join
SETTINGS_PATH = abspath(dirname(__file__))
DIR_PROJ = abspath(join(SETTINGS_PATH, '../../'))

sys.path.append(DIR_PROJ)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mydata14.settings'

import django.core.handlers.wsgi


#application = django.core.handlers.wsgi.WSGIHandler()
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    environ['SCRIPT_NAME'] = ''
    return _application(environ, start_response)

