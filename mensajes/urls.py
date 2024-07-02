
from django.urls import path
from . import views

urlpatterns = [
    path('private/<str:username>/', views.private_chat, name='private_chat'),
    path('get_users/', views.get_users, name='get_users'),
  
]
