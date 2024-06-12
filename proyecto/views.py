from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_home')  # O la página que quieras después del login
        else:
            error_message = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
            return render(request, 'inicio/login.html', {'error_message': error_message})
    return render(request, 'inicio/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Por favor, inicia sesión.')
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = UserCreationForm()
    return render(request, 'inicio/registro.html', {'form': form})
