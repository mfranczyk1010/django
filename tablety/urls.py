from django.urls import path
from tablety.views import wszystkie_tablety, nowy_tablet, edytuj_tablet, usun_tablet

urlpatterns = [
    path('wszystkie/', wszystkie_tablety, name="wszystkie_tablety"),
    path('nowy/', nowy_tablet, name="nowy_tablet"),
    path('edytuj<int:id>', edytuj_tablet, name="edytuj_tablet"),
    path('usun/<int:id>', usun_tablet, name="usun_tablet")
]