from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Log(models.Model):
    file_name = models.CharField(max_length = 256)
    file_size = models.BigIntegerField()
    downloaded_from = models.CharField(max_length = 1024)
    download_status = models.IntegerField()
    pos_to_seek = models.BigIntegerField()
