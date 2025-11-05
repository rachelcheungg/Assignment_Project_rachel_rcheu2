from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from matplotlib import pyplot as plt
from django.http import HttpResponse
from login.models import User
from search.models import Website
from io import BytesIO
import requests

class UserFavoritesAPI(View):
    def get(self, request):
        users = User.objects.all()

        results = []
        for user in users:
            favorite_websites = Website.objects.filter(favorites__user=user).values("website_name")
            results.append({
                "user": user.username,
                "favorites": list(favorite_websites)
            })

        data = {
            "count": len(results),
            "results": results
        }
        return JsonResponse(data)

import json
import urllib.request
from django.urls import reverse
from django.views.generic import TemplateView

class FavoritesChartPage(TemplateView):
    template_name = "personalization/favorite_count_chart.html"

def favorites_chart_png(request):
    api_url = request.build_absolute_uri(reverse("api_user_favorites"))

    with urllib.request.urlopen(api_url) as resp:
        payload = json.load(resp)

    results = payload.get("results", [])
    usernames = [r["user"] for r in results]
    favorite_counts = [len(r["favorites"]) for r in results]

    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=150)
    x = range(len(usernames))

    ax.bar(x, favorite_counts, color="#13294B")
    ax.set_title("Number of Favorite Websites per User")
    ax.set_xlabel("User")
    ax.set_ylabel("Number of Favorites")
    ax.set_xticks(list(x))
    ax.set_xticklabels(usernames, rotation=45, ha="right")

    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")

def api_ping_jsonresponse(request):
    users = User.objects.all()

    results = []
    for user in users:
        favorite_websites = Website.objects.filter(favorites__user=user).values("website_name")
        results.append({
            "user": user.username,
            "favorites": list(favorite_websites)
        })

    data = {
        "count": len(results),
        "results": results
    }
    return JsonResponse(data)


def api_ping_httpresponse(request):
    users = User.objects.all()

    results = []
    for user in users:
        favorite_websites = Website.objects.filter(favorites__user=user).values("website_name")
        results.append({
            "user": user.username,
            "favorites": list(favorite_websites)
        })

    data = {
        "count": len(results),
        "results": results
    }
    payload = json.dumps(data)
    return HttpResponse(payload, content_type="text/plain")


class LibraryBooks(View):
    def get(self, request):
        query = request.GET.get("q")
        params = {
            "q": query,
        }

        try:
            output_raw_all = requests.get("https://openlibrary.org/search.json?q=<query>", params=params, timeout=5)

            output_raw_all.raise_for_status()
            output_polished_all = output_raw_all.json()

            output_polished_cw_only = output_polished_all.get("docs", [])

            filtered = []
            for doc in output_polished_cw_only:
                filtered.append({
                    "author": doc.get("author_name", []),
                    "book": doc.get("title")
                })

            return JsonResponse({"library": filtered})

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": str(e)}, status=502)
