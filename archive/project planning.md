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
* [ ] We also need to keep track of different properties of cards in the card database to update the model later and different attribute of the user preferences to use for the recommender predictions. 
* [ ] For geographic features we need to know which banks the user wants to consider to learn the number of atms and number of offices near a particular radius. 
* [ ] Add user preference model with one to one relationship with user.

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



* [ ] Forms : 