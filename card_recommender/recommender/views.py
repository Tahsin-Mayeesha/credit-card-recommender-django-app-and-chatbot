from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from .forms import ContactForm,PreferenceForm
from .models import Card
from django.views.generic.edit import FormView
import numpy as np
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import itertools
from .recommender import feature_list,generate_recommendations
from sklearn.externals import joblib


def homepage(request):
    return render(request, 'home.html')



class PreferenceView(FormView):
    template_name = 'preferences.html'
    form_class = PreferenceForm
    success_url = '/recommendations/'

    
        
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        card_type = form.cleaned_data['card_type']
        interest_rate = form.cleaned_data['interest_rate']
        max_credit_limit = form.cleaned_data['max_credit_limit']
        visa_vs_mastercard = form.cleaned_data['visa_vs_mastercard']
        bank = form.cleaned_data['bank']
        rewards = form.cleaned_data['rewards']
        
        user_input = list(itertools.chain(card_type,interest_rate,max_credit_limit,visa_vs_mastercard,bank,rewards))
        rec = generate_recommendations(feature_list,user_input)
        
        self.request.session['recommendation_indices'] = rec[0]
        self.request.session['recommendation_scores'] = rec[1]
        
    
        return super().form_valid(form)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    


class RecommendationListView(TemplateView):
    template_name = "recommendation_list.html"
    
    def test_card(self):
        recommendation_indices = self.request.session['recommendation_indices']
        recommendation_scores = self.request.session['recommendation_scores']
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

    return render(request, "contact/view.html", context)
    
    