# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    """用户"""
    telephone = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
