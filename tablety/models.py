from django.db import models

# Create your models here.
class Dostawca(models.Model):
    nazwa_dostawcy = models.CharField(max_length=64)

    def __str__(self):
        return self.nazwa_dostawcy


class Produkt(models.Model):
    producent = models.CharField(max_length=65, null=False)
    model = models.CharField(max_length=65, null=False)
    opis = models.TextField(max_length=65, null=False, default="")
    liczba_sztuk = models.PositiveSmallIntegerField(default=1)
    cena = models.DecimalField(max_digits=6,decimal_places=2,null=False,blank=True)
    zdjecie = models.ImageField(upload_to="zdjecia", null=True,blank=True)

    dostawca = models.ForeignKey(Dostawca,on_delete=models.CASCADE)

    def __str__(self):
        return self.producent_i_model()

    def producent_i_model(self):
        return "{} {}".format(self.producent,self.model)


class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5 )
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} - {} gwiazdek".format(self.produkt.producent,self.produkt.model, self.gwiazdki)
