from django.db import models
from usuarios.models import User


class AccesoFormacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    
class TeamsMeeting(models.Model):
    meeting_url = models.URLField(verbose_name="URL de la Reunión de Teams")

    def __str__(self):
        return "Reunión de Teams"


class TrainingSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams_url = models.URLField(verbose_name="URL de la Reunión de Teams")

    def __str__(self):
        return f"TrainingSession for {self.user.email}"