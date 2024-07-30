from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'content', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)

