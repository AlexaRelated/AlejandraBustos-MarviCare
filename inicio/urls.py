from django.urls import path
from . import views
from .views import zoom_view, generate_signature, home_view, mantenimiento_view
from .views import post_detail, cosmetica_view

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_posts, name='search_posts'),
    path('zoom/', zoom_view, name='zoom'),
    path('generate-signature/', generate_signature, name='generate_signature'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/edit/', views.create_or_update_post, name='edit_post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('cosmetica/', cosmetica_view, name='cosmetica'),
    path('maquillaje/', views.maquillaje_view, name='maquillaje'),
    path('dermocosmetica/', views.dermocosmetica_view, name='dermocosmetica'),
    path('perfumeria/', views.perfumeria_view, name='perfumeria'),
    path('formaciones/', views.formaciones_view, name='formaciones'),
    path('bienestar/', views.bienestar_view, name='bienestar'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('home/', home_view, name='home'),
    path('mantenimiento/', mantenimiento_view, name='mantenimiento'),
    path('about/', views.about_view, name='about'),
    path('buscar/', views.buscar_view, name='buscar'),
]
