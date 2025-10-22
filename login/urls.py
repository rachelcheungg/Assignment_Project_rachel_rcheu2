# code is from the week-4 demo

from django.urls import path, include
from . import views

urlpatterns = [
    path("http/", views.user_list, name='user-list-url'),     # HttpResponse View
    path("render/", views.user_list_render, name='user-list-render-url'),     # render() view
    path("users/", views.UserListView.as_view(), name='user-list'),   # class-based ListView
    path("function-add-user/", views.add_user, name="add-user-url"),
    path("user-contact/", views.user_contact, name="user-contact-url"),
    path("success/", views.success_view, name="success-url"),
    path("<str:username>/", views.UserDetailView.as_view(), name='user-detail-url'),
]