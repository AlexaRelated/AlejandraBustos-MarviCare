from django import forms
from inicio.models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')  # Agregamos 'name' y 'email' aquí

    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')

        
