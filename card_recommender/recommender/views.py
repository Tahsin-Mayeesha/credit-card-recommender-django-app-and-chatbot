from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm

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

#def recommendations(request):
#    return HttpResponse("Recommended Cards")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class RecommendationListView(TemplateView):
    template_name = "recommendation_list.html"
    
    def recommended_cards(self):
        return [{'name':"Card 1","bank":"Bank 1","score":0.987},
                {"name":"Card 2","bank":"Bank 2","score":0.765}]
        
        
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"contact",
        "content":"Welcome to the Contact page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
    #    #print(request.POST)
    #    print(request.POST.get('fullname'))
    #    print(request.POST.get('email'))
    #    print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
    
    