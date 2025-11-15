from django.urls import path
from . import views

#This is where we connect our views to URLs so that when a user visits that specific URL, they are shown the correct views.

#I had help with copoilt with making this file. The app_name = 'counter' line makes a namespace for the URLs in this app, which is useful when including these URLs in the project's main URL configuration to avoid name clashes with other apps.
#I had help from the Django documentation on URL dispatcher: https://docs.djangoproject.com/en/5.2/intro/tutorial01/
app_name = 'counter'

urlpatterns = [       
    path('', views.index, name='index'),
    path('add_food', views.add_food, name='add_food'),
    path('total_calories', views.total_calories, name='total_calories'),
    path('today/', views.today, name='today'),
]
