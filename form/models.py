# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=500, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    cep = models.CharField(max_length=10, blank=False)
    iptu_price = models.DecimalField(max_digits=8, decimal_places=2)
    neighbourhood = models.CharField(max_length=200, blank=True)
    optin = models.BooleanField(default=True, blank=False)

    def __unicode__(self):
        return self.name
