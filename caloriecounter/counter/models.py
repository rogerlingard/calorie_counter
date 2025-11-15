from django.db import models

# Create your models here.

#We created a model to store food items with their name, calories, servings, and creation date. We did with the sqlite3 database that is included with Django by default. 
#I used this model so that we could easily store and retrieve food items and their nutritional information for the calorie counter.
#I followed the Django documentation on models: https://docs.djangoproject.com/en/5.2/intro/tutorial02/
class Food(models.Model):
    food_name = models.CharField(max_length=100)
    calories = models.IntegerField()
    servings = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.food_name
    def total_calories(self):
        return self.calories * self.servings
