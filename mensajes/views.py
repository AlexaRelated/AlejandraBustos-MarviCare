
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje
from .forms import MensajeForm
from django.contrib import messages


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
    print(f"Usuario actual: {request.user.username}")
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    print(f"Mensajes recibidos para {request.user.username}: {mensajes_recibidos.count()}")
    
    for mensaje in mensajes_recibidos:
        print(f"Mensaje de {mensaje.remitente.username} a {mensaje.destinatario.username} - Asunto: {mensaje.asunto}")
    
    return render(request, 'mensajes/bandeja_entrada.html', {})


@login_required
def redactar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            destinatario = form.cleaned_data['destinatario']
            asunto = form.cleaned_data['asunto']
            contenido = form.cleaned_data['contenido']
            
            # Crear el objeto Mensaje y guardarlo en la base de datos
            mensaje = Mensaje(destinatario=destinatario, asunto=asunto, contenido=contenido, remitente=request.user)
            mensaje.save()

            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja_entrada')  # Utiliza el nombre de vista definido en urls.py
    else:
        form = MensajeForm()
    
    return render(request, 'mensajes/redactar.html', {'form': form})