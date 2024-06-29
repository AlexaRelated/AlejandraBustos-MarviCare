
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    # Lógica para mostrar la bandeja de entrada de mensajes
    return render(request, 'mensajes/inbox.html', {})

@login_required
def enviar_mensaje(request, username):
    destinatario = User.objects.get(username=username)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.destinatario = destinatario
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form, 'destinatario': destinatario})

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes_recibidos': mensajes_recibidos})


def redactar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            destinatario_id = form.cleaned_data['destinatario']
            destinatario = User.objects.get(id=destinatario_id)
            asunto = form.cleaned_data['asunto']
            contenido = form.cleaned_data['contenido']
            mensaje = Mensaje(emisor=request.user, destinatario=destinatario, asunto=asunto, contenido=contenido)
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('inbox')  # Redirecciona a la bandeja de entrada
    else:
        form = MensajeForm()
    return render(request, 'mensajes/redactar.html', {'form': form})