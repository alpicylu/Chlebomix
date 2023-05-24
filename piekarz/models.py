from django.db import models
from magazynier.models import Produkty

# Create your models here.
class Przepisy(models.Model):
    przepis_id = models.AutoField(primary_key=True)
    nazwa_przepisu = models.CharField(default='',unique=True , max_length=50)

class Skladniki(models.Model):
    #By default, since this model has no primary_key set explicitly,
    #it will have an auto generated BigAutoField. To make this more obvious
    #an Auto field was added manually
    krotka_id = models.AutoField(primary_key=True)
    # przepis_id = models.IntegerField()
    przepis = models.ForeignKey(Przepisy, on_delete=models.CASCADE, null=True)
    # produkt_id = models.IntegerField()
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE, null=True)
    ilosc_produktu = models.FloatField(default=0.0)

    class Meta:
        unique_together = ['przepis', 'produkt']
