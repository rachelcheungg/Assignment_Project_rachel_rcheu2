from django.urls import path, include
from . import views
from .views import category_counts_chart

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name='categories-list-url'),
    path("websites/", views.WebsiteListView.as_view(), name='website-list-cbv'),
    path("charts/categories.png", category_counts_chart, name="chart-categories"),
]
