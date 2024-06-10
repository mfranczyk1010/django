from django.contrib import admin
from .models import Dostawca, Produkt, Ocena

# Register your models here.
@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['producent', 'model']
    search_fields = ['producent']



admin.site.register(Dostawca)
admin.site.register(Ocena)
