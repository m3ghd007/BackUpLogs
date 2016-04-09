

from django.http import HttpResponse, JsonResponse
from django.db import models
from models import Log
from django.core import serializers

import json

def get_downloaded_logs(request):
    response = {}
    response['name'] = "Siddhartha"
    response['surname'] = "Sikder"

    return JsonResponse(response)
def add_log(request):
    return 'Ok'

def get_downloadables(request):
    json_resp = {}
    list = []
    downloaded = False
    for i in range(0, 5):
        file = [' '.join(['Dummy File', str(i)]), str(i * 10 + 1024), downloaded]
        downloaded = not downloaded
        list.append(file,)
    print list
    json_resp['files'] = list
    return JsonResponse(json_resp)
