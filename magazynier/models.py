from django.db import models
import uuid

# Create your models here.
class Produkty(models.Model):
    produkt_id = models.AutoField(primary_key=True)
    ilosc_dostepna = models.FloatField(default=0.0, blank=False, null=False, unique=False)
    nazwa_produktu = models.CharField(default='', max_length=30, blank=False, null=False, unique=True)
    
    
    
    
    