from import_export import resources
from .models import Recommendation,Card


        
class CardResource(resources.ModelResource):
    class Meta:
        model = Card
        
class RecommendationResource(resources.ModelResource):
    class Meta:
        model = Recommendation