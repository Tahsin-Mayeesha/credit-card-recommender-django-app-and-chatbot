from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Person, Card

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Card)
class CardAdmin(ImportExportModelAdmin):
    pass