import os, sys
home_dir = os.getenv("HOME")

from os.path import abspath, dirname, join
SETTINGS_PATH = abspath(dirname(__file__))
DIR_PROJ = abspath(join(SETTINGS_PATH, '../../'))


# ---------start old--------------

sys.path.append(home_dir + "/virtualenv/v4/lib/python2.7/site-packages/")
sys.path.append(DIR_PROJ)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mydata14.settings'

import django.core.handlers.wsgi

#application = django.core.handlers.wsgi.WSGIHandler()
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    environ['SCRIPT_NAME'] = ''
    return _application(environ, start_response)



# ---------start new?--------------

#import site
#site.addsitedir(home_dir + "/virtualenv/v4/lib/python2.7/site-packages/")

#site.addsitedir(DIR_PROJ)

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydata14.settings")


#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()




