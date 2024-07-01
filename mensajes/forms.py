from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all(), label='Destinatario')
    asunto = forms.CharField(max_length=100, label='Asunto')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']