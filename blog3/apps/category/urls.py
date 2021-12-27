from django.urls import path
from .views import *
from apps.category import views

urlpatterns = [
	path('', views.ListCategory.as_view(), name='category_list')
]