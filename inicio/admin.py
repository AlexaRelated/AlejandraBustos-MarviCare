
from django.contrib import admin
from .models import Post
from .forms import PostForm
from .models import Profile
from .models import Category, Entry

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Entry)
