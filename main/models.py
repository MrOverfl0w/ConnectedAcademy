from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

def createUser(data):
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    user = User.objects.create_user(email, name, password)
    user.save()

