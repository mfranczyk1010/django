from django.forms import  ModelForm
from  .models import Produkt

class ProduktForm(ModelForm):
    class Meta:
        model = Produkt
        fields = ['producent', 'model', 'opis', 'cena', 'zdjecie', 'dostawca']