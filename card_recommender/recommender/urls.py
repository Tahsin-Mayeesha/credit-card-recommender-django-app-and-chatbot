from django.urls import path
from .views import PreferenceView,SignUp,RecommendationListView,contact_page,ProfileView,ProductDetailView
from django.views.generic.base import TemplateView # new
from django.conf.urls import url


urlpatterns = [path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
               path('preferences/',PreferenceView.as_view(),name="preferences"),
               path('recommendations/',RecommendationListView.as_view(),name="recommendations"),
               path('signup/', SignUp.as_view(), name='signup'),
               path('contact/', contact_page,name='contact'),
               url('products/(?P<pk>\d+)/$', ProductDetailView.as_view(),name='detail'),
]
                         