from django.contrib import admin
from .models import Post, BlogPost, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
