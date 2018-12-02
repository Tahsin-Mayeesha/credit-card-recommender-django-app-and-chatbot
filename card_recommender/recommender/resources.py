from import_export import resources
from .models import Person, Card

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        
class CardResource(resources.ModelResource):
    class Meta:
        model = Card