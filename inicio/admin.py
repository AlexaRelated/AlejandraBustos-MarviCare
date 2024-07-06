from django.contrib import admin
from .models import Post, Profile, Category, Entry, ContactMessage, ComentarioPost  

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    fields = ('title', 'content', 'image', 'category')  
    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # Si no hay autor asignado
            obj.author = request.user
        super().save_model(request, obj, form, change)

class ComentarioPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'autor', 'fecha_publicacion')
    list_filter = ('post', 'fecha_publicacion')
    search_fields = ('contenido', 'autor__username')
    readonly_fields = ('fecha_publicacion',)

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(ContactMessage)
admin.site.register(ComentarioPost, ComentarioPostAdmin)
