# PAST ISSUES

* [x] Get the home, profile,about and recommendations page views created and urlpattern configured by using functions.

```python
# in urls.py project level directory

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('boards.urls')),
]

# in urls.py app level directory

from django.urls import path,include
from .views import home,about

urlpatterns = [path('', home,name="home"),
               path('about/', about, name = "about")]
               
# in views.py

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About Page")
```



* [x] Models : We need to know which user has been recommended which cards. A card can be recommended to multiple users. A user can be recommended multiple cards. A recommender "relationship" has extra attribute recommendation score. Note : Made the model using custom many to many model.
* [x] We also need to keep track of different properties of cards in the card database to update the model later.

``` python
# Working with objects in shell

from example.models import Company
google = Company(name="Google")
google.save() # saving an object to the database.

# Getting an object from database.

from example.models import Company
google = Company.objects.get(pk=1) # pk = primary key

# updating attribute 
google.name = Alphabet.

# foreign key example 
# in models file

from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
		
class Programmer(models.Model):
	name = models.CharField(max_length=20)
	company = models.ForeignKey(Company,on_delete = models.CASCADE)
	
	def __str__():
		return self.name

# inside the shell.

from example.models import Company,Programmer
apple = Company.objects.get(pk=1)
arvin = Programmer(name="Arvin", company=apple) # pass the foreignkey object
arvin.save()

# to find all objects associated with one object

# like all programmers associated with a company

microsoft.programmer_set.all()
	
```





# Current Issues

* [ ] Geographical features : If I incorporate geographical features in prediction time based on user address/latitude or longitude, I'll have to fit the model again and again for each user which does not make sense. Key idea therefore is to incorporate two separate scores, location score based on how close the bank and bank atms are to the user address based on google places api search, and what sort of cards the user is looking for based on the preference score. Combination of the two scores need to be done based on some method e.g average, scaling etc. Then the final results are based on the combination scores with the top 5 scoring cards.
* [ ] Forms and form validation : Django makes form validation extremely easy with Formview and form fields. But what's the based way to pass data between views? Right now I've two separate views for user preference form and recommendations results. The data needs to go from user preference form, to the recommender predict method. The recommendation prediction scores and indices has to go to the recommendation result view. Then the final output is going to go to recommendation result page by using class methods for views. If this is the general workflow, what's the best way to find the POST data from the recommendations page? Writing form validation should not take much time. 
* [ ] Email sending upon model update : 
* [ ] Structuring the chatbot project :  