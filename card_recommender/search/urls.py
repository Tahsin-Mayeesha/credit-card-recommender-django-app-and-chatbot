from django.conf.urls import url

from .views import (SearchProductView)



urlpatterns = [

    url('$', SearchProductView.as_view(), name='query'),





]