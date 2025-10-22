from django.urls import path, include
from . import views
from .views import FeedbackView

urlpatterns = [
    path("http/", views.user_list, name='user-list-url'),     # HttpResponse View
    path("render/", views.user_list_render, name='user-list-render-url'),     # render() view
    path("users/", views.UserListView.as_view(), name='user-list'),   # class-based ListView
    path("add-user/", views.add_user, name="add-user-url"),
    path("user-contact/", views.user_contact, name="user-contact-url"),
    path('feedback/', FeedbackView.as_view(), name='feedback-form'),
    path("success/", views.success_view, name="success-url"),
    path("<str:username>/", views.UserDetailView.as_view(), name='user-detail-url'),
]