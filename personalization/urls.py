from django.urls import path, include
from .views import UserFavoritesAPI, favorites_chart_png

urlpatterns = [
    path("api/user-favorites/", UserFavoritesAPI.as_view(), name="api_user_favorites"),
    path("charts/favorites.png", favorites_chart_png, name="favorites-chart-png"),
]