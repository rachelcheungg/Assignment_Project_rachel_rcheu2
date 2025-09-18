from django.db import models
from django.conf import settings

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    website = models.ForeignKey("Website", on_delete=models.CASCADE)