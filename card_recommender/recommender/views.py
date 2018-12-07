from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return HttpResponse("About Page")

def user_preference(request):
    return HttpResponse("User Profile Page")

def recommendations(request):
    return HttpResponse("Recommended Cards")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'