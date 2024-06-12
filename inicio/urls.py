from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view_cuentas, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view_cuentas, name='signup'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/', views.post_list, name='post_list'),
    path('maquillaje/', views.maquillaje_posts, name='maquillaje_posts'),
    path('category/cosmetica/', views.category_cosmetica, name='category_cosmetica'),
    path('category/maquillaje/', views.category_maquillaje, name='category_maquillaje'),
    path('category/dermocosmetica/', views.category_dermocosmetica, name='category_dermocosmetica'), 
    path('category/perfumeria/', views.category_perfumeria, name='category_perfumeria'),
    path('category/formaciones/', views.category_formaciones, name='category_formaciones'),
    path('category/contacto/', views.category_contacto, name='category_contacto'),
]
