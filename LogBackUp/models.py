from __future__ import unicode_literals

from django.db import models

# Create your models here.

import json;

class LogUser(models.Model):
    user_name = models.CharField(max_length = 64)

    def __str__(self):
        return user_name

class Remote(models.Model):
    host_name = models.CharField(max_length = 1024)
    directory = models.CharField(max_length = 2048)
    remote_user = models.ForeignKey(LogUser)

    def __init__(self, name, dir):
        host_name = name
        directory = dir

    def __str__(self):
        return json.dump(self)

class Log(models.Model):
    file_name = models.CharField(max_length = 256)
    file_size = models.BigIntegerField()
    download_status = models.IntegerField()
    pos_to_seek = models.BigIntegerField()

    downloaded_from = models.ForeignKey(Remote)

    def __init__(self, name, size):
        file_name = name
        file_size = size

    def __str__(self):
        return json.dump(self)
