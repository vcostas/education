"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SILENCED_SYSTEM_CHECKS = ['django_mysql.W003','django_mysql.W001', 'models.E006']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4@lfqhr$9c0)5t30ly4r++t7m=!!buu+zgiuer8p--kremfg@j'

#Dias que es valido el token de reseteo de contraseña
PASSWORD_RESET_TIMEOUT_DAYS = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
            'libraries': {
            },
            'debug': DEBUG,
        },
    },
]

ALLOWED_HOSTS = ['127.0.0.1']

SITE_ID = 1

INSTALLED_APPS = (
    'django_adminlte',
    'django_adminlte_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_mysql',
    'guardian',
    'app',
    'bootstrap3',
    'security',
    'adm',
    'memcache',
    'sitemessage.apps.SitemessageConfig',
)


AUTH_PROFILE_MODULE = 'security.models.UserProfile'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.SessionTimeoutMiddleware.SessionTimeoutMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

GUARDIAN_RENDER_403 = True
GUARDIAN_RAISE_403 = False

SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=3600 #Default: 1209600 (2 weeks, in seconds)
SESSION_EXPIRE_SECONDS = 600
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True


ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fameghino',
        'USER': 'root',
        'PASSWORD': 'Karizma@123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8',
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "sistemaDeNotas/../static"),
    os.path.join(BASE_DIR, "sistemaDeNotas/../static/js"),
    os.path.join(BASE_DIR, "sistemaDeNotas/../static/images"),
]
#STATICFILES_FINDERS = [
#    'djangobower.finders.BowerFinder',
#]

BOWER_COMPONENTS_ROOT = BASE_DIR +'/components/'

BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap3'
)

# Media directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOG_DIR = os.path.join(BASE_DIR, 'log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'log/sige.log',
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 0,
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s|%(message)s'
        },
    },
    'loggers': {
        'sistemaDeNotas.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sistemaDeNotas.tasks': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sistemaDeNotas.management': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sistemaDeNotas.models': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
