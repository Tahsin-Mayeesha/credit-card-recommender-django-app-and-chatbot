# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:00:33 2018

@author: user
"""

from django.urls import path,include
from .views import homepage,aboutpage,user_preference,recommendations

urlpatterns = [path('', homepage,name="home"),
               path('about/', aboutpage, name = "about"),
               path('preferences/',user_preference,name="preferences"),
               path('recommendations/',recommendations,name="recommendations"),
               ]