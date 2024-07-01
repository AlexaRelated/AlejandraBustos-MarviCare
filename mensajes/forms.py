from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)