"""
Project main settings file. These settings are common to the project
if you need to override something do it in local.pt
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path

from decouple import config

# PATHS
# Path containing the django project
BASE_DIR = Path(__file__).parent.parent.parent

# Path of the top level directory.
# This directory contains the django project, apps, libs, etc...
PROJECT_ROOT = os.path.dirname(BASE_DIR)
SECRET_KEY = config('SECRET_KEY')
# SITE SETTINGS
# https://docs.djangoproject.com/en/2.0/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '.optoutools.com', 'api.optoutools.com']

# https://docs.djangoproject.com/en/2.0/ref/settings/#installed-apps
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'django.contrib.staticfiles',
    # Local apps
    'opt_out.public_api.api',
]

# DEBUG SETTINGS
# https://docs.djangoproject.com/en/2.0/ref/settings/#debug
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('DB_HOST', default='127.0.0.1', cast=str),
        'PORT': config('DB_PORT', default=5432, cast=int),
    }
}
# https://docs.djangoproject.com/en/2.0/ref/settings/#internal-ips
INTERNAL_IPS = ('127.0.0.1',)

# LOCALE SETTINGS
# Local time zone for this installation.
# https://docs.djangoproject.com/en/2.0/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/2.0/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/2.0/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/2.0/ref/settings/#use-l10n
USE_L10N = False

# https://docs.djangoproject.com/en/2.0/ref/settings/#use-tz
USE_TZ = False

# MEDIA AND STATIC SETTINGS
# Absolute filesystem path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/2.0/ref/settings/#media-root
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media')

# URL that handles the media served from MEDIA_ROOT. Use a trailing slash.
# https://docs.djangoproject.com/en/2.0/ref/settings/#media-url
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# https://docs.djangoproject.com/en/2.0/ref/settings/#static-root
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public/static')

# URL prefix for static files.
# https://docs.djangoproject.com/en/2.0/ref/settings/#static-url
STATIC_URL = '/static/'

# Additional locations of static files
# https://docs.djangoproject.com/en/2.0/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# TEMPLATE SETTINGS
# https://docs.djangoproject.com/en/2.0/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# URL SETTINGS
# https://docs.djangoproject.com/en/2.0/ref/settings/#root-urlconf.
ROOT_URLCONF = 'opt_out.public_api.website.urls'

# MIDDLEWARE SETTINGS
# See: https://docs.djangoproject.com/en/2.0/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# LOGGING
# https://docs.djangoproject.com/en/2.0/topics/logging/
LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'level': "DEBUG"
        }
    }
}
