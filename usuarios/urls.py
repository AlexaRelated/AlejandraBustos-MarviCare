from django.urls import path
from . import views
from .views import ChatView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup_view_cuentas, name='signup'),
    path('login/', views.login_view_cuentas, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_views, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.profile_views, name='ver_perfil'),
    path('modificar/', views.update_profile, name='modificar_perfil'),
    path('chat/', views.ChatView.as_view(), name='chat'), 
    path('chat/<str:room_name>/', ChatView.as_view(), name='chat_room'),
]