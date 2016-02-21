# -*- coding: utf-8 -*-
u"""Arquivo de configuração do Django."""
import logging
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import normpath

from configurations import Configuration
from configurations import values


DJANGO_ROOT = dirname(abspath(__file__))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)


class Common(Configuration):
    u"""Configuração comum para todos os ambientes."""

    DEBUG = values.BooleanValue(False)
    ADMINS = values.SingleNestedTupleValue((
        ('Sergio Garcia', 'sergio@gestaolivre.org'),
    ))
    MANAGERS = values.SingleNestedTupleValue((
        ('Sergio Garcia', 'sergio@gestaolivre.org'),
    ))
    DATABASES = values.DatabaseURLValue('postgres://postgres@db/postgres')
    CACHES = values.CacheURLValue('locmem://')
    EMAIL = values.EmailURLValue('console://')
    EMAIL_SUBJECT_PREFIX = values.Value('[%s] ' % SITE_NAME)
    TIME_ZONE = values.Value('America/Sao_Paulo')
    LANGUAGE_CODE = values.Value('pt-br')
    USE_I18N = values.BooleanValue(True)
    USE_L10N = values.BooleanValue(True)
    USE_TZ = values.BooleanValue(True)
    MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
    MEDIA_URL = values.Value('/media/')
    STATIC_ROOT = values.PathValue(normpath(join(SITE_ROOT, 'assets')))
    STATIC_URL = values.Value('/assets/')
    STATICFILES_DIRS = (
        normpath(join(SITE_ROOT, 'bower_components')),
        normpath(join(SITE_ROOT, 'static')),
    )
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = []
    FIXTURE_DIRS = (
        normpath(join(SITE_ROOT, 'fixtures')),
    )
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
    MIDDLEWARE_CLASSES = [
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
        # 'gestaolivre.apps.core.middleware.GlobalRequestMiddleware',
    ]
    ROOT_URLCONF = '%s.urls' % SITE_NAME
    DJANGO_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.postgres',
        'django.contrib.humanize',
        'django.contrib.admin',
        'mptt',
        'django_mptt_admin',
        'widget_tweaks',
    )
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
    INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
    LOGIN_REDIRECT_URL = '/'
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
    WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
    MIGRATION_MODULES = {
    }
    INSTALLED_APPS += (
        'rest_framework',
        'rest_framework.authtoken',
        'corsheaders',
    )
    REST_FRAMEWORK = {
        'PAGE_SIZE': 10
    }
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
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

    @classmethod
    def pre_setup(cls):
        u"""Executado antes da Configuração."""
        super(Common, cls).pre_setup()

    @classmethod
    def setup(cls):
        u"""Executado depois da Configuração."""
        super(Common, cls).setup()
        logging.info('Configurações de produção carregadas: %s', cls)

    @classmethod
    def post_setup(cls):
        u"""Executado depois da Configuração."""
        super(Common, cls).post_setup()
        logging.debug("done setting up! \o/")


class Dev(Common):
    u"""Configuração para Desenvolvimento."""

    DEBUG = True
    SECRET_KEY = values.Value('(ec65w1as3rno#!g#e*4wji!m*6#$=6v5d-bs--%jax(7o_y6$')


class Prod(Common):
    u"""Configuração para Produção."""

    DEBUG = False
    EMAIL = values.EmailURLValue('smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True')
    ALLOWED_HOSTS = ['.gestaolivre.org']
