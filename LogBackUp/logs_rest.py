

from django.http import HttpResponse, JsonResponse
from django.db import models
from models import Log
from django.core import serializers


def get_downloaded_logs(request):
    response = {}
    response['name'] = "Siddhartha"
    response['surname'] = "Sikder"

    return JsonResponse(response)
def add_log(request):
    return 'Ok'
