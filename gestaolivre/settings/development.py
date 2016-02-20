# -*- coding: utf-8 -*-
"""Development settings and globals."""

from __future__ import absolute_import

from .base import *  # NOQA


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = True
# ######### END DEBUG CONFIGURATION


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.9/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ######### END EMAIL CONFIGURATION
