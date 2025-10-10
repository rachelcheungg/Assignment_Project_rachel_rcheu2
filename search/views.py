from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Category, Website
from django.db.models import Count, Q

# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'search/category_list.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["total_websites"] = Website.objects.count()

        ctx["websites_per_category"] = (
            Category.objects
            .annotate(n_websites=Count("websites"))
            .order_by("category_name")
        )

        return ctx


class WebsiteListView(View):
    def get(self, request):
        return render(
            request,
            'search/website_list.html',
            context={'websites': Website.objects.all()}
        )

