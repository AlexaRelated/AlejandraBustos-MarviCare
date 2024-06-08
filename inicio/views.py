from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def inicio(request):
    return HttpResponse ('Bienvenidos a mi inicio')

