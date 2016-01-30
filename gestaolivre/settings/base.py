# -*- coding: utf-8 -*-
"""Common settings and globals."""

from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import normpath
from sys import path

# ######### PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our python path, this way we don't need to type our
# project name in our dotted import paths:
path.append(DJANGO_ROOT)
# ######### END PATH CONFIGURATION


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = False
# ######### END DEBUG CONFIGURATION


# ######### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#admins
ADMINS = (
    ('Sergio Garcia', 'sergio@ginx.com.br'),
)

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#managers
MANAGERS = ADMINS
# ######### END MANAGER CONFIGURATION


# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
# ######### END DATABASE CONFIGURATION


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# ######### END EMAIL CONFIGURATION


# ######### CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ######### END CACHE CONFIGURATION


# ######### GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#time-zone
TIME_ZONE = 'America/Sao_Paulo'

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#language-code
LANGUAGE_CODE = 'pt-br'

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#use-tz
USE_TZ = True
# ######### END GENERAL CONFIGURATION


# ######### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#media-url
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION


# ######### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#static-url
STATIC_URL = '/assets/'

# See: https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'bower_components')),
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# ######### END STATIC FILE CONFIGURATION


# ######### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = '(ec65w1as3rno#!g#e*4wji!m*6#$=6v5d-bs--%jax(7o_y6$'
# ######### END SECRET CONFIGURATION


# ######### SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# ######### END SITE CONFIGURATION


# ######### FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
# ######### END FIXTURE CONFIGURATION


# ######### TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
            'debug': DEBUG
        },
    },
]
# ######### END TEMPLATE CONFIGURATION


# ######### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'roma.apps.core.middleware.GlobalRequestMiddleware',
)
# ######### END MIDDLEWARE CONFIGURATION


# ######### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
# ######### END URL CONFIGURATION


# ######### APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',

    # Third party apps
    'mptt',
    'django_mptt_admin',
    'widget_tweaks',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # 'gestaolivre.apps.core',
    # 'gestaolivre.apps.accounting',
    # 'gestaolivre.apps.br_accounting',
    # 'gestaolivre.apps.address',
    # 'gestaolivre.apps.banking',
    # 'gestaolivre.apps.br_nfse',
    # 'gestaolivre.apps.contact',
    # 'gestaolivre.apps.dashboard',
    # 'gestaolivre.apps.base',
    # 'gestaolivre.apps.pessoa',
    # 'gestaolivre.apps.empresa',
    # 'gestaolivre.apps.enderecamento',
)

# See: https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# ######### END APP CONFIGURATION


# ######### AUTHORIZATION

LOGIN_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# #########


# ######### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
# ######### END WSGI CONFIGURATION


# ########## TESTS CONFIGURATION
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# ########## END TESTS CONFIGURATION


# ########## MIGRATIONS CONFIGURATION
MIGRATION_MODULES = {
}
# ########## END MIGRATIONS CONFIGURATION


# ########### API CONFIGURATION

INSTALLED_APPS += (
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
)

REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True

# ########### END API CONFIGURATION

# ######### COMPRESSOR CONFIGURATION
INSTALLED_APPS += (
    'compressor',
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc --source-map-map-inline {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)
# ######### END COMPRESSOR CONFIGURATION
