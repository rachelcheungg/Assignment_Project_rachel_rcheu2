from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Category, Website

# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'search/category_list.html'
    context_object_name = 'category_list'


class WebsiteListView(View):
    def get(self, request):
        return render(
            request,
            'search/website_list.html',
            context={'websites': Website.objects.all()}
        )

