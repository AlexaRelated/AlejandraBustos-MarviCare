from django.urls import path
from . import views as inicio_views
from . import views
from django.urls import path
from .views import post_detail

urlpatterns = [
    path('', inicio_views.index, name='index'),  # Página de inicio de inicio
    path('login/', inicio_views.login_view_cuentas, name='login'),
    path('logout/', inicio_views.logout_view, name='logout'),
    path('signup/', inicio_views.signup_view_cuentas, name='signup'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('maquillaje/', views.maquillaje_posts, name='maquillaje_posts'),
]
