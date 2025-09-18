from django.db import models
from login.models import User
from search.models import Website
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey("login.User", on_delete=models.CASCADE)
    website = models.ForeignKey("search.Website", on_delete=models.CASCADE)