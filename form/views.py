# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from models import Client
from serializers import ClientSerializer

# Create your views here.


class CreateClient(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

