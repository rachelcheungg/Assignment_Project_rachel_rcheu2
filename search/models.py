from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.category_name}"


class Website(models.Model):
    id = models.AutoField(primary_key=True)
    website_address = models.URLField(unique=True, max_length=200)
    website_name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='websites')

    def __str__(self):
        return f"{self.website_name} | {self.website_address}"