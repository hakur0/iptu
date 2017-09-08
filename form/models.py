# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=500, blank=False)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=False)
    iptu_price = models.DecimalField(max_digits=8, decimal_places=2)
    neighbourhood = models.CharField(max_length=200, blank=True)
    optin = models.BooleanField(default=True, blank=True)
    email_phone = models.CharField(max_length=200, blank=False, null=True)

    def __unicode__(self):
        if self.neighbourhood:
            return '{0}, que mora em {1} e paga {2} reais'.format(self.name, self.neighbourhood, self.iptu_price)
        else:
            return '{0}, que paga {1} reais'.format(self.name, self.iptu_price)
