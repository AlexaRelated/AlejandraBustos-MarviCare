
from django.urls import path
from . import views

urlpatterns = [
    path('enviar/<str:username>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('inbox/', views.bandeja_entrada, name='inbox'),
    path('redactar/', views.redactar_mensaje, name='redactar_mensaje'),
    path('inbox/', views.inbox, name='inbox'),
    path('', views.inbox, name='inbox'),  # URL para la bandeja de entrada de mensajes
  
]
