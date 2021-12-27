import contextlib
from typing import ContextManager
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.post.models import Post
from .forms import PostCreationForm

class ListPosts(ListView):
    model = Post
    template_name = 'posts/posts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-published_date')
        return context
	
"""     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_popular_post'] = Post.objects.filter()
        return context """

class DetailPost(DetailView):
	model = Post
	template_name='detail_post.html'


class CreatePost(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostCreationForm
	success_url = '/'
	template_name = 'post/post_create.html'
	fields = [
		'title',
		'content',
		'image',
	]

class UpdatePost(LoginRequiredMixin, UpdateView):
	model = Post
	form_class = PostCreationForm
	template_name = 'posts/post_create.html'
	success_url='/'
	fields = [
		'title',
		'content',
		'image',
	]

class DeletePost(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('lista')