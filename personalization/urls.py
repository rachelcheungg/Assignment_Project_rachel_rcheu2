from django.urls import path, include
from .views import UserFavoritesAPI

urlpatterns = [
    path("api/user-favorites/", UserFavoritesAPI.as_view(), name="api_user_favorites"),
]