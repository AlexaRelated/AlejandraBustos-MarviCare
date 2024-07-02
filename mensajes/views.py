
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User


@login_required
def private_chat(request, username):
    return render(request, 'mensajes/private_chat.html', {
        'room_name': f'private-{username}',
        'other_user': username,
    })

def get_users(request):
    users = User.objects.values('username')
    return JsonResponse({'users': list(users)})