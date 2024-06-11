from django.contrib import admin
from .models import Post
from inicio.models import Post

for post in Post.objects.all():
    print(post.slug)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'category', 'image')
        }),
    )

admin.site.register(Post, PostAdmin)



