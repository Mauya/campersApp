# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10, verbose_name='Gender', default='Male')
    organisation = models.CharField(max_length=20, verbose_name='Organisation', default="")
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email