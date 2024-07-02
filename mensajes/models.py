from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    autor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    sala = models.CharField(max_length=255, default="public")

    def __str__(self):
        return f'{self.autor} to {self.receptor}: {self.mensaje[:20]}'
