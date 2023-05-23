from django.shortcuts import render
from magazynier.models import Produkty
from piekarz.models import Przepisy, Skladniki

# Create your views here.
def homeView(request):
    # przepis = Przepisy.objects.get(przepis_id=1)
    # skladniki = Skladniki.objects.get(przepis.przepis_id)
    # nazwy_skladnikow = []
    # for s in skladniki:
    #     nazwy_skladnikow.append(Produkty.objects.get(produkt_id=s.produkt_id))

    # context = {
    #     "przepis_id": przepis.przepis_id,
    #     "nazwa_przepisu": przepis.nazwa_przepisu,
    #     "nazwy_skladnikow": nazwy_skladnikow,
    #     "skladniki": skladniki
    # }

    return render(request, 'home.html', {})