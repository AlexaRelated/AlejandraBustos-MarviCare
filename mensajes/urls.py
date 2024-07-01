
from django.urls import path
from . import views

urlpatterns = [
    path('bandeja-entrada/', views.bandeja_entrada, name='bandeja_entrada'),
    path('redactar/', views.redactar_mensaje, name='redactar_mensaje'),
    path('ver-mensaje/<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
    path('private/<str:username>/', views.private_chat, name='private_chat'),
    path('get_users/', views.get_users, name='get_users'),
  
]
