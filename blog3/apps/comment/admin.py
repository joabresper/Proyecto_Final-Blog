from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')

admin.site.register(Comment, CommentAdmin)