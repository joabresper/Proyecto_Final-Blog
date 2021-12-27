from django.urls import path
from .views import *
from apps.post import views

urlpatterns= [
	path('', views.ListPosts.as_view(), name='list'),
	path('<slug:pk>/detalle', views.DetailPost.as_view(), name='detail'),
	path('<slug:pk>/modificar', views.UpdatePost.as_view(), name='update'),
	path('<slug:pk>/borrar', views.DeletePost.as_view(), name='delete'),
	path('crear/', views.CreatePost.as_view(), name='create')
]