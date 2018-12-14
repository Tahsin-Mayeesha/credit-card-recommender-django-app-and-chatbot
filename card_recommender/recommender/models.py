from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Card(models.Model):
    card_name  = models.CharField(max_length=150)
    bank_name  = models.CharField(max_length=150)                  
    url    = models.CharField(max_length=300)                                   
    card_type = models.CharField(max_length=100)                   
    interest_rate = models.FloatField(null=True,blank=True)
    cash_withdrawal_limit_per_transaction = models.FloatField(null=True,blank=True)
    cash_withdrawal_limit_per_day = models.FloatField(null=True,blank=True)
    max_credit_limit = models.FloatField(null=True,blank=True)
    international_transaction_available = models.BooleanField(default =False)   
    balance_transfer_available  = models.BooleanField(default =False)               
    dual_currency  = models.BooleanField(default =False)                            
    reward_supplementary_card = models.BooleanField(default =False)                  
    reward_airport_lounge     = models.BooleanField(default =False)                 
    reward_cashback_available = models.BooleanField(default =False)                 
    reward_luxary_resort_hotel= models.BooleanField(default =False)                 
    reward_insurance_plan     = models.BooleanField(default =False)                 
    reward_travel_benefits    = models.BooleanField(default =False)                 
    reward_fine_dining        = models.BooleanField(default =False)                 
    reward_buffet_discount    = models.BooleanField(default =False)                 
    reward_medical_discount   = models.BooleanField(default =False)                 
    reward_shopping           = models.BooleanField(default =False)                 
    reward_airlines_ticket    = models.BooleanField(default =False)                 
    reward_point_program      = models.BooleanField(default =False)                 
    reward_emi_available      = models.BooleanField(default =False)
    users = models.ManyToManyField(User,
                                   through="Recommendation",
                                   through_fields = ('card','user'))

class Recommendation(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recommendation_score = models.FloatField()
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    
    TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    )
    
    title = models.CharField(max_length=3, choices=TITLE_CHOICES,null=True)
     

