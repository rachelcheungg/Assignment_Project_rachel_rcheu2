from django.urls import path, include
from .views import UserFavoritesAPI, favorites_chart_png, FavoritesChartPage

urlpatterns = [
    path("api/user-favorites/", UserFavoritesAPI.as_view(), name="api_user_favorites"),
    path("charts/favorite_count/", FavoritesChartPage.as_view(), name="favorites-chart-page"),
    path("charts/favorites.png", favorites_chart_png, name="favorites-chart-png"),
]