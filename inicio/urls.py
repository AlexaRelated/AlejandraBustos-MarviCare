from django.urls import path
from . import views
from .views import search_posts, post_list, post_detail, create_post

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view_cuentas, name='signup'),
    path('login/', views.login_view_cuentas, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inicio/posts/', views.post_list, name='post_list'),
    path('', post_list, name='post_list'),
    path('search/', search_posts, name='search_posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),  # Esta es la única URL para crear un post
    path('post/<int:post_id>/edit/', views.create_or_update_post, name='edit_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('maquillaje/', views.maquillaje_posts, name='maquillaje_posts'),
    path('category_cosmetica/', views.category_cosmetica, name='category_cosmetica'),
    path('category_maquillaje/', views.category_maquillaje, name='category_maquillaje'),
    path('category_dermocosmetica/', views.category_dermocosmetica, name='category_dermocosmetica'),
    path('category_perfumeria/', views.category_perfumeria, name='category_perfumeria'),
    path('category_formaciones/', views.category_formaciones, name='category_formaciones'),
    path('category_contacto/', views.category_contacto, name='category_contacto'),
]
