from inspect import signature
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import BlogPost, Comment
from .forms import CommentForm
from django.http import JsonResponse
import time
import base64
import hmac
import hashlib
from .models import Category, Post, Author, Article

def index(request):
    posts = BlogPost.objects.all()  # Obtener todos los posts de BlogPost
    posts = []
    return render(request, 'inicio/index.html', {'posts': posts})

def home_view(request):
    return render(request, 'inicio/home.html')

def buscar_view(request):
    query = request.GET.get('q')
    resultados_tu_modelo2 = BlogPost.objects.filter(Q(campo__icontains=query))

def signup_view_cuentas(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(reverse('inicio/index.html'))  # Redirige a una vista principal o de inicio
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'inicio/login.html')

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
    posts = []
    return render(request, 'inicio/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def category_view(request, category_name):
    category = Category.objects.get(name__iexact=category_name)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', {'posts': posts})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

def maquillaje_posts(request):
    posts = Post.objects.filter(category='maquillaje')
    return render(request, 'maquillaje.html', {'posts': posts})

def category_cosmetica(request):
    posts = BlogPost.objects.filter(category='cosmetica')
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
    # Lógica para generar la firma
    return JsonResponse({'signature': signature})


def maquillaje_posts(request):
    posts = BlogPost.objects.filter(category='maquillaje')
    return render(request, 'maquillaje.html', {'posts': posts})

def cosmetica_view(request):
    posts = Post.objects.filter(tags__name__in=["cosmética"])
    return render(request, 'cosmetica.html', {'posts': posts})

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_success')
    else:
        form = CommentForm()
    comments = Comment.objects.all().order_by('-created_date')
    return render(request, 'inicio/contacto.html', {'form': form, 'comments': comments})

def comment_success_view(request):
    return render(request, 'comment_success.html')

def mantenimiento_view(request):
    return render(request, 'inicio/mantenimiento.html')

def about_view(request):
    return render(request, 'inicio/about.html')