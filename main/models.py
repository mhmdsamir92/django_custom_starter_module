from __future__ import unicode_literals
from django.db.models import Model, CharField


class Survey(Model):
    name = CharField(max_length=200)
    address = CharField(max_length=200)
    email = CharField(max_length=200)
    phone_number = CharField(max_length=200)
