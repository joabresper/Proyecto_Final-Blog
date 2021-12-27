from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date')
    list_filter = ('author', 'category', 'published_date')

admin.site.register(Post, PostAdmin)