from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Home Page")

def aboutpage(request):
    return HttpResponse("About Page")

def user_preference(request):
    return HttpResponse("User Profile Page")

def recommendations(request):
    return HttpResponse("Recommended Cards")