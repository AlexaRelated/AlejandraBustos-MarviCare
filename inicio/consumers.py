
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Lógica para conectar al WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Lógica para desconectar del WebSocket
        pass

    async def receive(self, text_data):
        # Lógica para recibir datos del WebSocket
        pass
