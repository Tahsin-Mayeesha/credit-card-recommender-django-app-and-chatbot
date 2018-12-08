from django.urls import path
from .views import aboutpage,PreferenceView,SignUp,RecommendationListView,contact_page
from django.views.generic.base import TemplateView # new


urlpatterns = [path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
               path('about/', aboutpage, name = "about"),
               path('preferences/',PreferenceView.as_view(),name="preferences"),
               path('recommendations/',RecommendationListView.as_view(),name="recommendations"),
               path('signup/', SignUp.as_view(), name='signup'),
               path('contact/', contact_page,name='contact'),

               ]