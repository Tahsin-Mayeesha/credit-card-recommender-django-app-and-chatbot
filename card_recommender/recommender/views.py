from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm,PreferenceForm
from .models import Card
# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return HttpResponse("About Page")

#def user_preference(request):
#    return render(request,'preferences.html')

#def recommendations(request):
#    return HttpResponse("Recommended Cards")
    
from django.views.generic.edit import FormView

class PreferenceView(FormView):
    template_name = 'preferences.html'
    form_class = PreferenceForm
    success_url = '/recommendations/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class RecommendationListView(TemplateView):
    template_name = "recommendation_list.html"
    
    def recommended_cards(self):
        return [{'name':"Card 1","bank":"Bank 1","score":0.987},
                {"name":"Card 2","bank":"Bank 2","score":0.765}]
    
    def test_card(self):
        recommendation_indices = [13,45,87,23,11]
        recommendation_scores = [0.98,0.54,0.32,0.30,0.24]
        results = []
        for index in [0,1,2,3,4]:
            card = Card.objects.get(pk=recommendation_indices[index])
            result_dict = {}
            result_dict['card_name'] = card.card_name
            result_dict['bank_name'] = card.bank_name
            result_dict['url'] = card.url
            result_dict['score'] = recommendation_scores[index]
            results.append(result_dict)
        return results
    
            
        
        
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
    
    