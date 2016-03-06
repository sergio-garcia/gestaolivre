# -*- coding: utf-8 -*-
u"""Configuração do aplicativo cadastro."""

from django.apps import AppConfig
# from django.core import checks
# from django.contrib.auth.checks import check_user_model
# from django.db.models.signals import post_migrate

# from .management import create_default_domain


class CadastroConfig(AppConfig):
    u"""Configuração do aplicativo cadastro."""

    name = 'gestaolivre.apps.cadastro'
    verbose_name = 'cadastro'

    # def ready(self):
    #     checks.register(checks.Tags.models)(check_user_model)
    #     post_migrate.connect(create_default_domain, sender=self)
