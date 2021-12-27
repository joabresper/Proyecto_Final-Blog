# import re
from django import forms
# from django.forms.fields import ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.user.models import Author

class AuthorForm(forms.ModelForm):
	picture = forms.ImageField(required=False, label="Foto")


	class Meta:
		model = Author
		fields = ("picture",)

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True, label="Nombre")
	last_name = forms.CharField(required=True, label="Apellido")

	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"email",
			"password1",
			"password2",
		)

class UserUpdateForm(forms.ModelForm):

	first_name = forms.CharField(required=True, label="Nombre")
	last_name = forms.CharField(required=True, label="Apellido")

	class Meta:
		model = User
		fields = (
			"first_name",
			"last_name",
		)
