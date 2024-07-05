
from django.urls import path
from . import views
from .views import ChatView

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('private-chat/<str:username>/', views.private_chat, name='private_chat'),
    path('get-users/', views.get_users, name='get_users'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('chat/<str:room_name>/', ChatView.as_view(), name='chat_room'),
]