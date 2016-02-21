# -*- coding: utf-8 -*-
u"""Configurações de URL do Gestão Livre."""

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
