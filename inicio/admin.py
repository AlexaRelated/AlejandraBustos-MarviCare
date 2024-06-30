from django.contrib import admin
from .models import Post, Profile, Category, Entry

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    fields = ('title', 'content', 'image', 'category')  # No incluir 'author' si se asigna automáticamente

    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # Si no hay autor asignado
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Entry)
