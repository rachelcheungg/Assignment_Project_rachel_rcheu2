from django.urls import path, include
from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name='categories-list-url'),
    path("websites/", views.WebsiteListView.as_view(), name='website-list-cbv'),
]
