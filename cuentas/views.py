from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def inicio(request):
    return HttpResponse ('Bienvenidos a mi inicio')

def template1(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1> Mi Template 1</h1> -- Fecha: {fecha}')