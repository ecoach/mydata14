import socket
host = socket.gethostname()

if host == "ecoach2.lsa.umich.edu":
    HOST = "DEVELOPMENT"
elif host == "ecoach3.lsa.umich.edu":
    HOST = "PRODUCTION"
else:
    HOST = "LOCAL"

# Django settings for ecoach project.
import django.template
django.template.add_to_builtins('django.templatetags.future')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# globals
DB_NAME    = 'ecoach7'
DPROJ_NAME = 'mydata7'
MPROJ_NAME = 'mts7'
COACH_NAME = 'Physics 135,140,235,240: Fall 2013'
COACH_URL = 'coach7'
COACH_EMAIL = 'ecoach-help@umich.edu'

from os.path import abspath, dirname, join
SETTINGS_PATH = abspath(dirname(__file__))
DIR_PROJ = abspath(join(SETTINGS_PATH, '../')) + '/'
DIR_NTS = DIR_PROJ + DPROJ_NAME + '/' + MPROJ_NAME + "/Static/mts/js/nts/"
DIR_UPLOAD_DATA = DIR_PROJ + DPROJ_NAME + "/uploads/"
DIR_DOWNLOAD_DATA = DIR_PROJ + DPROJ_NAME + "/downloads/"
DIR_MYDATA = DIR_PROJ + DPROJ_NAME + '/'
#DOMAIN = 'ecoach.lsa.umich.edu'
DOMAIN = 'localhost'
DOMAIN_COACH = '/' + COACH_URL + '/'
URL_SUB = MPROJ_NAME + '/'

MYDATA = 'mydata7'

DATABASE_ROUTERS = ['mycoach.routers.UserRouter', 'mycoach.routers.CommonRouter']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
        'USER': 'ecoach',                      # Not used with sqlite3.
        'PASSWORD': 'ecoach',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'common': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'common1',                      # Or path to database file if using sqlite3.
        'USER': 'ecoach',                      # Not used with sqlite3.
        'PASSWORD': 'ecoach',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = DIR_PROJ + 'staticroot/' + DPROJ_NAME 
#STATIC_ROOT = DIR_PROJ + 'staticroot/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/' + DPROJ_NAME + '/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DIR_PROJ + '/' + DPROJ_NAME + '/' + MPROJ_NAME + '/Static',
    DIR_PROJ + 'static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ngs5ktl8wkkba0!dfad5g6$fhzx_zt=#lndi3!61emw#n5!+kj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

if HOST == "PRODUCTION" or HOST == "DEVELOPMENT":
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.RemoteUserMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )
else:
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = DPROJ_NAME + '.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DIR_PROJ + 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    DPROJ_NAME,
    'myselector',
    'mycoach',
    'mypublisher',
    'myusage',
    'myemailer',
    'nts',
    'myloader',
    'myexporter',
    'mylogger',
    'djangotailoring',
    'djangotailoring.surveys',
    'djangotailoring.tracking',
    # Uncomment the next line to enable the admin:
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'mycoach.UserProfile'

if HOST == "PRODUCTION" or HOST == "DEVELOPMENT":
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'mycoach.backends.SettingsBackend',
    )

LOGIN_URL = '/coaches/login/'

LOGIN_REDIRECT_URL = '/coaches/'

TAILORING2_PROJECT_ROOT = DIR_PROJ + DPROJ_NAME + '/' + MPROJ_NAME + '/'

#TAILORING2_PROJECT_CONFIG = DIR_PROJ + "tailoring2/config.py"
#or
TAILORING2_DICTIONARY = "mts.dictionary"
#and
TAILORING2_CUSTOMIZATION_MODULE = 'Utilities/Tool Support/application.py'

TAILORING2_SUBJECT_LOADER_CLASS = DPROJ_NAME + '.subjects.ECoachSubjectLoader'
#TAILORING2_DEBUG

