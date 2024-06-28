from django import forms
from inicio.models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image', 'slug']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']  # Incluye todos los campos que deseas mostrar en el formulario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tu nombre'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí'})