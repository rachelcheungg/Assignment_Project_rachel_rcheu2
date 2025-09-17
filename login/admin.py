from django.contrib import admin
from .models import Users, Websites, Favorites
# Register your models here.

admin.site.register(Users)
admin.site.register(Websites)
admin.site.register(Favorites)