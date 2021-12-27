from django.views.generic import ListView

from .models import Category

class ListCategory(ListView):
    model = Category
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context             
    
