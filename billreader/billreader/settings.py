# Django settings for billreader project.
import os
import json
import djcelery
import tastypie
djcelery.setup_loader()

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Kyle Corbitt', 'kylecorbitt@gmail.com')
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if 'DOTCLOUD_ENVIRONMENT' in os.environ:
	with open('/home/dotcloud/environment.json') as f:
  		dotcloud_env = json.load(f)
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		        'NAME': 'readerdb',                      # Or path to database file if using sqlite3.
		        'USER': dotcloud_env['DOTCLOUD_DB_SQL_LOGIN'],                      # Not used with sqlite3.
		        'PASSWORD': dotcloud_env['DOTCLOUD_DB_SQL_PASSWORD'],                  # Not used with sqlite3.
		        'HOST': dotcloud_env['DOTCLOUD_DB_SQL_HOST'],                      # Set to empty string for localhost. Not used with sqlite3.
		        'PORT': int(dotcloud_env['DOTCLOUD_DB_SQL_PORT']),                      # Set to empty string for default. Not used with sqlite3.
		    }
		}
		#credentials for the RabbitMQ task queue backend
		BROKER_HOST = dotcloud_env['DOTCLOUD_QUEUE_AMQP_HOST']
		BROKER_PORT = int(dotcloud_env['DOTCLOUD_QUEUE_AMQP_PORT'])
		BROKER_USER = dotcloud_env['DOTCLOUD_QUEUE_AMQP_LOGIN']
		BROKER_PASSWORD = dotcloud_env['DOTCLOUD_QUEUE_AMQP_PASSWORD']
		BROKER_VHOST = '/'
	
#Local test settings
else:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'readerdb',                      # Or path to database file if using sqlite3.
	        'USER': 'reader',                      # Not used with sqlite3.
	        'PASSWORD': 'homecomingvancandy',                  # Not used with sqlite3.
	        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
	        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	    }
	}
	#Celery connection to RabbitMQ 
	BROKER_URL = 'amqp://reader:homecomingvancandy@dev1'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
if 'DOTCLOUD_ENVIRONMENT' in os.environ:
	MEDIA_ROOT = '/home/dotcloud/data/'
else:
	MEDIA_ROOT = '/home/kyle/proj/bill_reader/web/billreader/data/'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/dotcloud/current/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://billreader-kyle.dotcloud.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nkzhynmyeu!al+(@tq_milp)#p)u(@o=c8z16l3h%wwllmvpt5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'billreader.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'billreader.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    #Locally defined apps
    'ATTparser',
    'djcelery',
    'tastypie',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
