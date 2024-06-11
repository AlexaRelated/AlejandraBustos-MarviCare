
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'inicio/index.html', {'posts': posts})

def login_view_cuentas(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'inicio/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view_cuentas(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'inicio/signup.html', {'form': form})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'article.html', {'post': post})
