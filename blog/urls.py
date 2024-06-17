from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('article/<int:pk>/', views.article, name='article'),
    path('author/<int:id>/', views.author_view, name='author'),
    path('category/<str:category>/', views.category_view, name='category_view'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]