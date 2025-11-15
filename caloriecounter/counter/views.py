from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.utils import timezone
from django.db.models import Sum, F, ExpressionWrapper, FloatField
from .models import Food
from .forms import FoodForm
# Create your views here.

#This is where we define the logic for handling requests and returning responses for our calorie counter app.

#I started out following the Django documentation on views: https://docs.djangoproject.com/en/5.2/intro/tutorial01/
#Then I eventually added more complex views like total_calories by using the help of copilot and the Django documentation on aggregation: https://docs.djangoproject.com/en/5.2/topics/db/aggregation/

#This view first takes in a web request. Then we get all the food objects from the database ordered by food_name.
#Then we create a string output that joins all the food names with a comma and space.
#Finally we render the index.html template with the food_list and output context variables.
def index(request):
    food_list = Food.objects.order_by("food_name")
    output = ", ".join([f.food_name for f in food_list])
    return render(request, "counter/index.html", {"food_list": food_list, "output": output})


#I had the help of copilot for this view
#This is a view that calculates the total calories from all food items in the database.
#It uses an expression to multiply calories and servings for each food item, aggregates the total using Sum, and returns the result as a JSON response.
#The JSON response ensures that the total is in a format suitable for web APIs.
def total_calories(request):

    expr = ExpressionWrapper(F('calories') * F('servings'), output_field=FloatField())
    total = Food.objects.aggregate(total=Sum(expr))['total'] or 0

    # Ensure JSON serializable (float)
    return JsonResponse({'total': float(total)})

#I had the help of copilot for this view as well.
#The today view first gets the current local date. It then filters the Food objects to get only those created today, ordered by creation time.
#It calculates the total calories for today's foods using an expression and aggregation, similar to the total_calories view.
#we then render the today.html template with the foods and total context variables.
def today(request):
    """Show foods added today and the total calories for today."""

    today_date = timezone.localdate()
    qs = Food.objects.filter(created_at__date=today_date).order_by('created_at')

    expr = ExpressionWrapper(F('calories') * F('servings'), output_field=FloatField())
    total = qs.aggregate(total=Sum(expr))['total'] or 0

    return render(request, 'counter/today.html', {'foods': qs, 'total': float(total)})


# Used Claude to generate this function. The function takes in a web request. With that request we see if the method is POST. If it is we create a form variable with the POST data. If the form is valid we save the form and redirect to the index page.
# If the method is not POST we create an empty form instance. We then get all food objects and render the add_food.html template with the form and foods context.
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counter:index')
    else:
        form = FoodForm()
    foods = Food.objects.all()
    return render(request, "counter/add_food.html", {"form": form, "foods": foods})