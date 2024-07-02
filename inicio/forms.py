from django import forms
from inicio.models import Post
from .models import Comment
from .models import ComentarioPost
from .models import Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']

class ComentarioPostForm(forms.ModelForm):
    class Meta:
        model = ComentarioPost
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')  

    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)

        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)