from django.contrib import admin
from .models import Food

# Register your models here.

#This was more for the exploration of Django's admin interface. By registering the Food model here, we can manage food items directly through the Django admin site.
admin.site.register(Food)