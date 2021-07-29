from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
#To create a view, we have to create a function
def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
