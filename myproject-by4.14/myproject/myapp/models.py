# -*- coding: utf-8 -*-
from django.db import models
from .validators import validate_file_extension

class Document(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    description = models.TextField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',validators=[validate_file_extension])