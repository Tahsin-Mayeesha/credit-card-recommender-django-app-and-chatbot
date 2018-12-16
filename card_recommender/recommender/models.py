from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q


# Create your models here.

class ProductQuerySet(models.query.QuerySet):
    #def active(self):
    #   return self.filter(active=True)


    #def featured(self):
    #    return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = Q(card_name__icontains=query) | Q(bank_name__icontains=query)
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    #def all(self):
    #    return self.get_queryset().active()

    #def features(self):
    #    return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


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
    
    objects = ProductManager()

    def __str__(self):
        return self.card_name
    
    def get_absolute_url(self):
        #return "/products/{pk}/".format(pk=self.pk)
        return reverse("detail", kwargs={"pk": self.pk})
    
class Recommendation(models.Model):
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recommendation_score = models.FloatField()
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=300)
    area = models.CharField(max_length=300)
    city = models.CharField(max_length=300)

