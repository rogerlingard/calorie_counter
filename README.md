# Overview

The web app that I wrote is a calorie calculator/tracker. It takes the food you submit, stores it in a database, and shows the tracked foods on one webpage and the ones you added for the day on another page. You can also click a button to see the total amount of calories that have been consumed or tracked.

Start the console, your starting directory should be the .\calorie_counter directory, and you then cd into the calorie_counter directory. Your path should now be .\calorie_couner\caloriecounter. Now you type python manage.py runserver to start the server. Click the link that appears towards the bottom of the command that ran. It should look something like this: "Starting development server at http://127.0.0.1:8000/", and you would click the link provided. 

After clicking the link, you will be brought to the http://127.0.0.1:8000/ webpage. You will then need to edit the link so that it says "http://127.0.0.1:8000/counter/" and then hit enter. You are now at the index page of the calorie counter web app. You can navigate to the counter/add_food and counter/today page by using the provided buttons on the webpage.

With this app, I am trying to learn about web apps and how they work. I specifically chose Django to use a bit of my Python knowledge to help make the web app and to focus more on the integration of it all. I believe that learning web applications will be good for knowing the basic principles of website interaction. I also wanted to prove to myself that I could learn about web apps, which was a topic that I knew was a weak area for me.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Calorie Calculator Demonstration Video](https://youtu.be/fh3KozgiHdE)

# Web Pages

counter/ (the index page)
*This page dynamically shows the entries from the Food database. We use the view to process the data from the database and pass it to the HTML page to dynamically show the table on the index page. We use a for loop to make the table dynamically show how many food entries are in it. We also have a total calories button that uses JavaScript to listen for whether the user clicked the total calorie button, and when they clicked, we got the information from the total_calorie view that returns a JsonResponse back to the JavaScript so that we can add an HTML paragraph tag with the total amount of calories. This view also has buttons that redirect you to the add_food page and the today webpage.

counter/add_food
*This page renders a form that the user can input data into. We use the view to dynamically name the fields of the form and also validate what data the user is going to be inputting into the form, so that it is able to line up with what we have in the database. When the submit button is clicked, it creates a food object that we will add to the model we have for the database. We also have a button that brings us back to the Food list on the page.

counter/today
*This page is very similar to the index page, but it now shows the food that has been added today, along with the time it was added. So the today view gets the foods that were created today by querying the database to see which foods fall under that criterion. We also get the total of calories that the queried result and return it so that the today.html page can dynamically create the table with the foods that were added today and show the total amount of calories for each food added today. You also have a button to go back to the index page. 
# Development Environment

*Visual Studio Code - Version 1.10.60
*Python - Version 3.9.13
*Django - Version 4.2.25
*SQLite3 - default, built-in with Django
*git - Version 2.42.0.windows.2

Libraries:
 - Django shortcuts: render, redirect, get_object_or_404
 - Django http: Http404, HttpResponse, JsonResponse
 - Django timezones: timezone
 - Django db: 
 - Django db. models: Sum, F, ExpressionWrapper, FloatField
 - Django apps: AppConfig
 - Django URLs: path

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Django Documentation Website](https://docs.djangoproject.com/en/5.2/)
* [Django Documentation tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
* [Dave Gray's YouTube Courses on YouTube](https://youtu.be/Rp5vd34d-z4?si=YU1ey9JwbTuk8dqN)
* [FreeCodeCamp.org's Django tutorial on YouTube](https://youtu.be/0roB7wZMLqI?si=4nsDy3HjQ_MnyES_)
* [Django Documentation Forms](https://docs.djangoproject.com/en/5.2/topics/forms/)

# Future Work
* Add a nutrition Database, editing the current one we have, so that we can have nutritional information in a database 
* Using the Nutrition Database created about, use some JavaScript to make an interactive breakdown wheel of the different nutritional facts
* Make the index page something that can be filtered and dynamically updated with user input. Adding a way to get rid of redundant entries. 
* Make a way for the user to use past food entries to reuse them for the form submission.

