from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SubscriptionForm 


@login_required
def index(request):
    # Lógica para mostrar la página de inicio
    return render(request, 'index.html')


def signup_view_cuentas(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.save()
            raw_password = form.cleaned_data.get('contraseña1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'inicio/signup.html', {'form': form})

def login_view_cuentas(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Nombre de usuario')
            password = form.cleaned_data.get('Contraseña')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('index')  # Redirigir a la página de inicio después del inicio de sesión
            else:
                messages.error(request, 'Usuario o contraseña invalido')
        else:
            messages.error(request, 'Datos de formulario no válidos')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    return render(request, 'inicio/profile.html', {'user': request.user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'inicio/update_profile.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # Lógica para manejar la suscripción
            messages.success(request, 'Te has suscrito con éxito.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, proporciona un correo electrónico válido.')
    else:
        form = SubscriptionForm()
    
    return render(request, 'inicio/registro.html', {'form': form})