from django.shortcuts import render, get_object_or_404
from .models import Post, BlogPost, Author, Article, Category, Comment
from .forms import CommentForm
from django.db.models import Q
from inicio.models import Post as InicioPost

def blog_home(request):
    posts = Post.objects.all().order_by('-id')  # Cargar todos los posts y ordenarlos por el ID en orden descendente
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

def crear_publicacion(request):
    # Lógica para crear una nueva publicación
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

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
