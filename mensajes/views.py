
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import JsonResponse

class ChatView(TemplateView):
    template_name = 'mensajes/chat.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los usuarios para enviarlos a la plantilla
        context['connected_users'] = User.objects.all()
        return context

@login_required
def private_chat(request, username):
    return render(request, 'mensajes/private_chat.html', {
        'other_user': username,
    })

def get_users(request):
    users = User.objects.values('username')
    return JsonResponse({'users': list(users)})

def room(request, room_name):
    return render(request, 'mensajes/room.html', {
        'room_name': room_name
    })

def get_users(request):
    users = User.objects.values('username')
    return JsonResponse({'users': list(users)})

def room(request, room_name):
    return render(request, 'mensajes/room.html', {
        'room_name': room_name
    })
