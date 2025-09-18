from django.db import models

# Create your models here.
class Website(models.Model):
    website_id = models.AutoField(primary_key=True)
    website_name = models.CharField(max_length=100)
    website_address = models.URLField(max_length=200)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)