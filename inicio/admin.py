from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug')
    search_fields = ('title', 'content')
    list_filter = ('categories',)  
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'categories', 'image')  
        }),
    )