
from django.urls import path
from . import views
from . import consumers
from .views import ChatView, private_chat, get_users, room


urlpatterns = [
    path('get_users/', views.get_users, name='get_users'),
    path('<str:room_name>/', views.room, name='room'),
    path('ws/chat/', views.ChatView.as_view(), name='chat'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('chat/<str:username>/', private_chat, name='private_chat'),
    path('get_users/', get_users, name='get_users'),
    path('room/<str:room_name>/', room, name='room'),
]


websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]