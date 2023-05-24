from django import forms
from .models import Produkty

class ProduktyRestockForm(forms.ModelForm):
    class Meta:
        model = Produkty
        fields = [
            "ilosc_dostepna"
        ]

class ProduktyRemoveForm(forms.ModelForm):
    class Meta:
        model = Produkty
        fields = [
            "ilosc_dostepna",
            "nazwa_produktu"
        ]