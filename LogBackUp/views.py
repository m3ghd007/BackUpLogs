from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

def index(request):
    return render(request, 'index.html', Context({'person':'Sid'}))

