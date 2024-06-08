from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'category', 'image')
        }),
    )

admin.site.register(Post, PostAdmin)
