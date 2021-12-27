""" from django.shortcuts import render
from django.views.generic import vi """

# from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from apps.user.forms import AuthorForm, UserForm, UserUpdateForm
from apps.user.models import Author

class AuthorCreateView(CreateView):
	template_name = "accounts/user_form.html"
	form_class = UserForm
	success_url = reverse_lazy("list")

	def form_valid(self, form):
		user = form.save()
		Author.objects.create(user=user)
		return super().form_valid(form)

class AuthorUpdateView(View):
	def get(self, request, *args, **kwargs):
		author_form = AuthorForm(instance=request.user.author)
		user_form = UserUpdateForm(instance=request.user)
		context = {"author_forms": author_form, "user_form": user_form}
		return render(request, "accounts/user_update.html", context=context)

	def post(self, request, *args, **kwargs):
		author_form = AuthorForm(request.POST, request.FILES, instance=request.user.author)
		user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
		if author_form.is_valid() and user_form.is_valid():
			user_form.save()
			author_form.save()
		return redirect("user_update") 

