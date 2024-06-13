from django.contrib import admin
from .models import Post
from inicio.models import Post
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'category', 'image')
        }),
    )


for post in Post.objects.all():
    if not post.slug:
        print(f"El post {post.title} no tiene slug.")


