from django.contrib import admin
from .models import User, Website, Favorite
# Register your models here.

admin.site.register(User)
admin.site.register(Website)
admin.site.register(Favorite)