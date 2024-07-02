from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile 

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico', required=True)
    first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellido', max_length=100)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'bio', 'numero_tienda', 'ciudad', 'avatar']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    city = forms.CharField(max_length=100, required=True, label='Ciudad')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    phone_number = forms.CharField(label='Número de teléfono', max_length=20)
    
    