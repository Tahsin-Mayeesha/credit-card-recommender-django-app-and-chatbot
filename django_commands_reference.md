* [ ] Get the home, profile,about and recommendations page views created and urlpattern configured by using functions.

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



* [ ] Models : In the recommendations model we need to keep track of which user has been recommended which card for future use. We also need to keep track of different properties of cards in the card database to update the model later and different attribute of the user preferences to use for the recommender predictions. For geographic features we need to know which banks the user wants to consider to learn the number of atms and number of offices near a particular radius. Right now I already have the card database model. What I need : 
  * [ ] add card_id to card model.
  * [ ] add profile model which has a one on one relationship with the user
  * [ ] add recommendation model which is to keep track of which user was given which recommendations from our model.