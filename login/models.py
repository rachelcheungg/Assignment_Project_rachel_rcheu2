from django.db import models

# Create your models here.
# Parent Table
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    username = models.CharField(max_length=11)

class Websites(models.Model):
    website_id = models.AutoField(primary_key=True)
    website_name = models.CharField(max_length=100)
    website_address = models.URLField(max_length=200)

class Favorites(models.Model):
    pk = models.CompositePrimaryKey("user_id", "website_id")
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    website = models.ForeignKey("Websites", on_delete=models.CASCADE)
