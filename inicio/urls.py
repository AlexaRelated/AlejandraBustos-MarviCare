from django.urls import path
from . import views
from .views import search_view
from .views import category_view


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/category/<str:category>/', category_view, name='category_view'),
    path('posts/', views.post_list, name='post_list'),
    path('blog/', views.blog_home, name='blog_home'),
    path('article/<int:pk>/', views.article, name='article'),
    path('author/<int:id>/', views.author_view, name='author'),
    path('category/<str:category>/', views.category_view, name='category_view'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('comienza-el-aprendizaje/', views.all_posts, name='all_posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('add_comment/<str:slug>/', views.add_comment, name='add_comment_slug'),
    path('search/', search_view, name='search_view'),
    path('zoom/', views.zoom_view, name='zoom'),
    path('generate-signature/', views.generate_signature, name='generate_signature'),
    path('post/<int:post_id>/edit/', views.create_or_update_post, name='edit_post'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('cosmetica/', views.cosmetica_view, name='cosmetica'),
    path('maquillaje/', views.maquillaje_view, name='maquillaje'),
    path('dermocosmetica/', views.dermocosmetica_view, name='dermocosmetica'),
    path('perfumeria/', views.perfumeria_view, name='perfumeria'),
    path('formaciones/', views.formaciones_view, name='formaciones'),
    path('bienestar/', views.bienestar_view, name='bienestar'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('home/', views.home_view, name='home'),
    path('mantenimiento/', views.mantenimiento_view, name='mantenimiento'),
    path('about/', views.about_view, name='about'),
    path('buscar/', views.buscar_view, name='buscar_view'),
    path('usuarios/chat/', views.index, name='chat'),
    
    ]
