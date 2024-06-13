from django.urls import path
from .views import login_view_cuentas, index, signup_view_cuentas, logout_view, post_list, post_detail, maquillaje_posts, category_cosmetica, category_maquillaje, category_dermocosmetica, category_perfumeria, category_formaciones, category_contacto

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_view_cuentas, name='signup'),
    path('login/', login_view_cuentas, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inicio/posts/', post_list, name='post_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('maquillaje/', maquillaje_posts, name='maquillaje_posts'),
    path('category_cosmetica/', category_cosmetica, name='category_cosmetica'),
    path('category_maquillaje/', category_maquillaje, name='category_maquillaje'),
    path('category_dermocosmetica/', category_dermocosmetica, name='category_dermocosmetica'),
    path('category_perfumeria/', category_perfumeria, name='category_perfumeria'),
    path('category_formaciones/', category_formaciones, name='category_formaciones'),
    path('category_contacto/', category_contacto, name='category_contacto'),
]
