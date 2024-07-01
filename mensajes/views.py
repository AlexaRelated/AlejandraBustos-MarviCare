
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
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes_recibidos': mensajes_recibidos})

@login_required
def redactar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja_entrada') 
    else:
        form = MensajeForm()
    
    return render(request, 'mensajes/redactar.html', {'form': form})

@login_required
def ver_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if mensaje.destinatario == request.user:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajes/ver_mensaje.html', {'mensaje': mensaje})


@login_required
def private_chat(request, username):
    return render(request, 'mensajes/private_chat.html', {
        'room_name': f'private-{username}',
        'other_user': username,
    })

def get_users(request):
    users = User.objects.all()
    users_list = [{'username': user.username} for user in users]
    return JsonResponse(users_list, safe=False)