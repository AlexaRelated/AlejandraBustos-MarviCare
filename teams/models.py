from django.db import models
from usuarios.models import User


class AccesoFormacion(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
    
class TeamsMeeting(models.Model):
    meeting_url = models.URLField(max_length=200)

    def __str__(self):
        return self.meeting_url


class TrainingSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams_url = models.URLField(verbose_name="URL de la Reunión de Teams")

    def __str__(self):
        return f"TrainingSession for {self.user.email}"