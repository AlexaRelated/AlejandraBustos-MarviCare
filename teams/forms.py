from django import forms
from .models import AccesoFormacion

class AccesoFormacionForm(forms.ModelForm):
    class Meta:
        model = AccesoFormacion
        fields = ['nombre', 'descripcion', 'fecha_inicio'] 
        
        
class YourForm(forms.Form):  # Puedes usar forms.ModelForm si está basado en un modelo
    campo = forms.CharField(max_length=100)  # Ajusta los campos según lo que necesites