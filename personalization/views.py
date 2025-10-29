from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from login.models import User
from search.models import Website

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