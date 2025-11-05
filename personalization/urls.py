from django.urls import path, include
from . import views
from .views import UserFavoritesAPI, favorites_chart_png, FavoritesChartPage, LibraryBooks

urlpatterns = [
    path("api/user-favorites/", UserFavoritesAPI.as_view(), name="api_user_favorites"),
    path("charts/favorite_count/", FavoritesChartPage.as_view(), name="favorites-chart-page"),
    path("charts/favorites.png", favorites_chart_png, name="favorites-chart-png"),

    path("api/ping-httpresponse/", views.api_ping_httpresponse, name="api-ping-httpresponse"),
    path("api/ping-json/", views.api_ping_jsonresponse, name="api-ping-json"),
    path("api/books/", LibraryBooks.as_view(), name="api-books"),
]