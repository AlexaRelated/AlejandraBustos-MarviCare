
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post, Author, Article, Category, BlogPost, Comment
from inicio.models import Post as InicioPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import BlogPost
from .models import Post, Comment
from .forms import CommentForm

def blog_home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts': posts})

def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article.html', {'post': post})

def article_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'article_detail.html', {'post': post})

def author_view(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'author.html', {'author': author})

def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', {'article': article})

def category_view(request, category):
    category_obj = get_object_or_404(Category, name__iexact=category)
    posts = Post.objects.filter(categories=category_obj)
    return render(request, 'category.html', {'category': category_obj, 'posts': posts})

def cosmetica_view(request):
    posts = Post.objects.all()
    blog_posts = BlogPost.objects.all()

    context = {
        'posts': posts,
        'blog_posts': blog_posts,
    }

    return render(request, 'inicio/cosmetica.html', context)

  

def crear_publicacion(request):
    return render(request, 'crear_publicacion.html')

def search_posts(request):
    query = request.GET.get('q')
    if query:
        inicio_posts = InicioPost.objects.filter(
            Q(title__icontains(query)) | Q(content__icontains(query))
        )
        blog_posts = BlogPost.objects.filter(
            Q(title__icontains(query)) | Q(content__icontains(query))
        )
        posts = list(inicio_posts) + list(blog_posts)
    else:
        posts = []
    return render(request, 'search_results.html', {'posts': posts, 'query': query})

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment(post=post, author=request.user, text=comment_text, created_at=timezone.now())
            comment.save()
            return redirect('post_detail', slug=post.slug)
    
    comments = post.comments.all()
    
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Incluir request.FILES para manejar archivos
        if form.is_valid():
            form.save()
            return redirect('blog_home')  # Redirigir a donde desees después de agregar la publicación
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def add_comment(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': form})