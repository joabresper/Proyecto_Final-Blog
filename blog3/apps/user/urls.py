""" from django.urls import path
from django.contrib.auth import views

urlpatterns = [
            path('login/',views.LoginView.as_view(), name='login'),
            path('logout/', views.logout_then_login, name='logout'),
] """

from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.user import views 

urlpatterns = [
        path("user/register/", views.AuthorCreateView.as_view(), name="user_register"),
        path("user/profile/", login_required(views.AuthorUpdateView.as_view()), name="user_update"),
]