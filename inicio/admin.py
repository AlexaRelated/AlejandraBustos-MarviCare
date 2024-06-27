from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  


