from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Post
from .forms import SignUpForm
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.text import slugify


def index(request):
    posts = Post.objects.exclude(slug__exact='')

    return render(request, 'inicio/index.html', {'posts': posts})

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

posts_without_slug = Post.objects.filter(slug='')
for post in posts_without_slug:
    post.slug = slugify(post.title)
    post.save()

def post_detail(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug)
    except Http404:
        return render(request, '404.html', {'error_message': 'Post no encontrado'})
    return render(request, 'article.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    active_tab = 'inicio'
    return render(request, 'inicio/post.html', {'posts': posts, 'active_tab': active_tab})

def maquillaje_posts(request):
    posts = Post.objects.filter(category='maquillaje')
    return render(request, 'maquillaje.html', {'posts': posts})

def category_cosmetica(request):
    posts = Post.objects.filter(category='cosmetica')
    return render(request, 'category_cosmetica.html', {'posts': posts})

def category_maquillaje(request):
    posts = Post.objects.filter(category='maquillaje')
    return render(request, 'category_maquillaje.html', {'posts': posts})

def category_dermocosmetica(request):
    posts = Post.objects.filter(category='dermocosmetica')
    return render(request, 'category_dermocosmetica.html', {'posts': posts})

def category_perfumeria(request):
    posts = Post.objects.filter(category='perfumeria')
    return render(request, 'category_perfumeria.html', {'posts': posts})

def category_formaciones(request):
    posts = Post.objects.filter(category='formaciones')
    return render(request, 'category_formaciones.html', {'posts': posts})

def category_contacto(request):
    posts = Post.objects.filter(category='contacto')
    return render(request, 'category_contacto.html', {'posts': posts})


