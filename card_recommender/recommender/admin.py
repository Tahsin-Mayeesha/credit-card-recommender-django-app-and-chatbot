from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Card,Recommendation


@admin.register(Card)
class CardAdmin(ImportExportModelAdmin):
    pass

@admin.register(Recommendation)
class RecommendationAdmin(ImportExportModelAdmin):
    pass