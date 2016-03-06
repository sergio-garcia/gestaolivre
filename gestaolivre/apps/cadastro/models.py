# -*- coding: utf-8 -*-
u"""Modelos padrões do Gestão Livre."""

import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models

from brazil_fields.fields import CNPJField
from brazil_fields.fields import CPFField

from .middleware import GlobalRequestMiddleware


def get_current_empresa(request=None):
    u"""Obtem a empresa selecionada através das informações do request."""
    if not request:
        request = GlobalRequestMiddleware.get_current_request()
    return request.user.domainuser.domains.first()


def get_current_empresa_pk(request=None):
    u"""Obtem a empresa selecionada através das informações do request."""
    return get_current_empresa(request).pk


class BaseModel(models.Model):
    u"""Modelo abstrato do Gestão Livre."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = JSONField(null=True)

    class Meta(object):
        abstract = True

    def __repr__(self):
        u"""Representação deste objeto."""
        return str(self)

    def __str__(self):
        u"""String que representa este objeto."""
        return '<{0}: {1}>'.format(self.__class__.__name__, self.id)


class Empresa(BaseModel):
    u"""Modelo abstrato especifico de uma empresa do Gestão Livre."""

    cnpj = CNPJField()

    class Meta(object):
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'


class PublicoModel(BaseModel):
    u"""Modelo compartilhado entre todas as empresas."""

    class Meta(object):
        abstract = True


class EmpresaModel(BaseModel):
    u"""Modelo privado de uma empresa."""

    empresa = models.ForeignKey(Empresa, default=get_current_empresa_pk)

    class Meta(object):
        abstract = True
