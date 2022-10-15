# Django views are Python functions that takes http requests and returns http response, like HTML documents.

# A web page that uses Django is full of views with different tasks and missions.

# Views are usually put in a file called views.py located on your app's folder.

# There is a views.py in your Home folder that looks like this:

# Home/views.py:

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is Home Page")

def About(request):
    return HttpResponse("This is About Us Page")


# Note : This is the simple example what content we want to show to users
# But How..?
# Now using URL we need to call views.py file and default it will run index file if we did not call any app name


