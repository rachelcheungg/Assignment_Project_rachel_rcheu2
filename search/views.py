from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Category, Website
from django.db.models import Count, Q
from io import BytesIO
from django.http import HttpResponse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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


def category_counts_chart(request):
    data = (
        Category.objects
        .annotate(website_count=Count("websites"))
        .order_by("category_name")
    )

    labels = [cat.category_name for cat in data]
    counts = [cat.website_count for cat in data]

    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)

    ax.bar(labels, counts, color="#13294B")

    ax.set_title("Websites per Category", fontsize=10, color="#13294B")

    ax.set_xlabel("Category", fontsize=8)
    ax.set_ylabel("Websites", fontsize=8)

    ax.tick_params(axis="x", rotation=45, labelsize=8)
    ax.tick_params(axis="y", labelsize=8)

    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")

    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type="image/png")