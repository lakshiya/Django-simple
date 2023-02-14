from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html",{})
    return HttpResponse("<h1> Welcome to view </h1>")

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html",{})
    # return HttpResponse("<h1> Welcome to contact page </h1>")

def about_view(request, *args, **kwargs):
    myContext = { "name": "Developed by Priya", "number" : "1234", "alist": ["Nitin","Priya","Scooby"]}
    return render(request, "about.html",myContext)
    # return HttpResponse("<h1> Welcome to about page </h1>")