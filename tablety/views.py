from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Produkt
from .forms import ProduktForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def wszystkie_tablety(request):
    wszystkie = Produkt.objects.all()
   # test = "test"
    return render(request, 'produkty.html', {"produkty": wszystkie})


@login_required
def nowy_tablet(request):
    form = ProduktForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_tablety)
    return render(request, 'nowy_tablet.html', {'form' : form})

@login_required
def edytuj_tablet(request, id):
    produkt = get_object_or_404(Produkt, pk=id)
    form = ProduktForm(request.POST or None, request.FILES or None, instance=produkt)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_tablety)
    return render(request, 'nowy_tablet.html', {'form': form, 'nowy': True})

@login_required
def usun_tablet(request, id):
    produkt = get_object_or_404(Produkt, pk=id)

    if(request.method == 'POST'):
        produkt.delete()
        return redirect(wszystkie_tablety)
    return render(request, 'potwierdz.html', {'produkt': produkt})