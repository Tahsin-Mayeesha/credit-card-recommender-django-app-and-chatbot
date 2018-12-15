from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from .forms import ContactForm,PreferenceForm,ProfileForm
from django.views.generic.edit import FormView
import numpy as np
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import itertools
from .recommender import feature_list,generate_recommendations,get_recommendations
from sklearn.externals import joblib
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import DetailView
from .models import Card,Profile

def homepage(request):
    return render(request, 'home.html')


class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = "profile.html"
    success_url = '/'
    
    def get_object(self, queryset=None):

        # get the existing object or created a new one
        obj, created = Profile.objects.get_or_create(user=self.request.user)

        return obj
    
    def form_valid(self, form):
        name = form.cleaned_data['username']
        print(name)
        return super().form_valid(form)

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
        rec = generate_recommendations(self.request.user,feature_list,user_input)
        
        return super().form_valid(form)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    


class RecommendationListView(TemplateView):
    template_name = "recommendation_list.html"
    
    def test_card(self):
        #recommendation_indices = self.request.session['recommendation_indices']
        #recommendation_scores = self.request.session['recommendation_scores']
        results = get_recommendations(self.request.user)
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
    
    
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
       context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
       print(context)
       return context


    def get_object(self, *args, **kwargs):
        request =self.request
        pk = self.kwargs.get('pk')
        instance = Card.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Card doesnt exist")
        return instance
