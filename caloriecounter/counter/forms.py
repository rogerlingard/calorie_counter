from django import forms
from .models import Food

# Form for adding a new food item, used for the add_food view.
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'servings', 'calories']