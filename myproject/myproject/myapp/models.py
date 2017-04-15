# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    description = models.TextField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
