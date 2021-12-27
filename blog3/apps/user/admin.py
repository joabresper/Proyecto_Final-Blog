""" from django.contrib import admin
from apps.user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff')

admin.site.register(User, UserAdmin) """

from django.contrib import admin
from apps.user.models import Author

admin.site.register(Author)