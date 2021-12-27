from django import forms
from .models import Post

class PostCreationForm(forms.ModelForm):
	class Meta:
		model= Post
		fields = [
				'title',
				'content',
				'image',
			]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		