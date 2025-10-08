from django.db import models
from login.models import User
from search.models import Website
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey("login.User", on_delete=models.CASCADE, related_name="favorites")
    website = models.ForeignKey("search.Website", on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "website"], name="unique_user_favorite_website"),
        ]
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username} | {self.website.website_name}"