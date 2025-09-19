from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(primary_key=True, unique=True, max_length=100)

    def __str__(self):
        return f"{self.category_name}"


class Website(models.Model):
    website_address = models.URLField(primary_key=True, unique=True, max_length=200)
    website_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.website_name} | {self.website_address}"