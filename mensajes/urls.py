
from django.urls import path
from . import views
from . import consumers

urlpatterns = [
    path('private/<str:username>/', views.private_chat, name='private_chat'),
    path('get_users/', views.get_users, name='get_users'),
    path('<str:room_name>/', views.room, name='room'),
]


websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]