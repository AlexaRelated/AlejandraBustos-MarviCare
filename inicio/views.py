from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Post, Category
from .forms import SignUpForm, PostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import BlogPost, Comment
from .forms import CommentForm
from .forms import ProfileForm
from django.http import JsonResponse
import time
import base64
import hmac
import hashlib


def index(request):
    posts = Post.objects.all()  # Obteniendo todos los posts
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

def search_posts(request):
    query = request.GET.get('q')
    if query:
        # Filtrar tanto los posts de inicio como los del blog
        inicio_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        blog_posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        # Unir los resultados en una única lista
        posts = list(inicio_posts) + list(blog_posts)
    else:
        posts = []
    return render(request, 'search_results.html', {'posts': posts, 'query': query})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirigir a la lista de posts después de crear un post
    else:
        form = PostForm()
    return render(request, 'inicio/create_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def create_or_update_post(request, post_id=None):
    # Si se proporciona un post_id, estamos editando un post existente
    if post_id:
        post = get_object_or_404(Post, pk=post_id)
    else:
        post = None

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(f'/post/detail/{post.id}')  # Redirige al detalle del post creado
    else:
        form = PostForm(instance=post)
    
    return render(request, 'inicio/create_or_update_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'inicio/post_list.html', {'posts': posts})

def category_view(request, category_name):
    category = Category.objects.get(name__iexact=category_name)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', {'posts': posts})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(categories=category)
    return render(request, 'inicio/category_posts.html', {'category': category, 'posts': posts})

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


def zoom_view(request):
    return render(request, 'zoom.html')

def generate_signature(request):
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    meeting_number = 'YOUR_MEETING_NUMBER'
    role = 0  # 0 para participante, 1 para anfitrión

    timestamp = int(time.time() * 1000) - 30000
    msg = f'{api_key}{meeting_number}{timestamp}{role}'
    message = base64.b64encode(bytes(msg, 'utf-8'))
    secret = bytes(api_secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    hash = base64.b64encode(hash.digest())
    signature = f'{api_key}.{meeting_number}.{timestamp}.{role}.{hash.decode("utf-8")}'

    return JsonResponse({'signature': signature})

def cosmetica_view(request):
    return render(request, 'inicio/cosmetica.html')

def maquillaje_view(request):
    return render(request, 'inicio/maquillaje.html')

def dermocosmetica_view(request):
    return render(request, 'inicio/dermocosmetica.html')

def perfumeria_view(request):
    return render(request, 'inicio/perfumeria.html')

def formaciones_view(request):
    return render(request, 'inicio/formaciones.html')

def bienestar_view(request):
    return render(request, 'inicio/bienestar.html')

def contacto_view(request):
    return render(request, 'inicio/contacto.html')