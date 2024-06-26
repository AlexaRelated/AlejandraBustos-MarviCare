from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup_view_cuentas(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Cargar el perfil del usuario
            user.profile.city = form.cleaned_data.get('city')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')  # Redirigir a la página de inicio después del registro
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
                messages.success(request, 'Login successful')
                return redirect('index')  # Redirigir a la página de inicio después del inicio de sesión
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def my_view(request):
    return render(request, 'my_template.html', {'user': request.user})

@login_required
def profile_view(request):
    return render(request, 'inicio/profile.html', {'user': request.user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'inicio/update_profile.html', {'form': form})