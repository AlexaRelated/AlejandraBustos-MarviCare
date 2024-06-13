from django.contrib import admin
from .models import Post, BlogPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author__username',)

# Registra los modelos restantes
admin.site.register(Post)  # Registrar Post sin especificar el admin
admin.site.register(BlogPost)