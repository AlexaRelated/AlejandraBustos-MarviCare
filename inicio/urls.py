
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import zoom_view, generate_signature

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('signup/', views.signup_view_cuentas, name='signup'),
    path('login/', views.login_view_cuentas, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('posts/', views.post_list, name='post_list'),
    path('search/', views.search_posts, name='search_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    path('create/', views.create_post, name='create_post'),
    path('zoom/', zoom_view, name='zoom'),
    path('generate-signature/', generate_signature, name='generate_signature'),
    path('post/<int:post_id>/edit/', views.create_or_update_post, name='edit_post'),
    path('maquillaje/', views.maquillaje_posts, name='maquillaje_posts'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('category_cosmetica/', views.category_cosmetica, name='category_cosmetica'),
    path('category_maquillaje/', views.category_maquillaje, name='category_maquillaje'),
    path('category_dermocosmetica/', views.category_dermocosmetica, name='category_dermocosmetica'),
    path('category_perfumeria/', views.category_perfumeria, name='category_perfumeria'),
    path('category_formaciones/', views.category_formaciones, name='category_formaciones'),
    path('category_contacto/', views.category_contacto, name='category_contacto'),
    path('cosmetica/', views.cosmetica_view, name='cosmetica'),
    path('maquillaje/', views.maquillaje_view, name='maquillaje'),
    path('dermocosmetica/', views.dermocosmetica_view, name='dermocosmetica'),
    path('perfumeria/', views.perfumeria_view, name='perfumeria'),
    path('formaciones/', views.formaciones_view, name='formaciones'),
    path('bienestar/', views.bienestar_view, name='bienestar'),
    path('contacto/', views.contacto_view, name='contacto'),
]
