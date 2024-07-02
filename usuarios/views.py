from profile import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, SubscriptionForm
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@login_required
def index(request):
    return render(request, 'index.html')

def signup_view_cuentas(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, 'Te has registrado con éxito.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
            print(form.errors)  # Imprime los errores del formulario en la consola
    else:
        form = SignUpForm()
    return render(request, 'inicio/signup.html', {'form': form})



def login_view_cuentas(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña inválidos.')
        else:
            messages.error(request, 'Datos de formulario no válidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio/login.html', {'form': form})

def logout_view(request):
    logout(request)  
    return redirect('login')

@login_required
def profile_views(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'profile': profile})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'usuarios/update_profile.html', {'form': form})

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


def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
