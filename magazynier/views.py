from django.shortcuts import render, get_object_or_404, redirect
from magazynier.models import Produkty
from django.http import HttpResponse
from .forms import ProduktyRestockForm, ProduktyRemoveForm
from django.contrib.auth.models import Permission

# Create your views here.
def show_storage(request):
    if request.method == "POST":
        product_to_remove = get_object_or_404(Produkty, produkt_id=request.POST.get("produkt_id"))
        product_to_remove.delete()

    permissions = Permission.objects.filter(user=request.user)
    obj = Produkty.objects.all()
    context = {
        "produkty": obj,
        "permissions": permissions
    }

    return render(request, "storage.html", context)

def restock_form(request, prod_id):
    # product_to_restock = Produkty.objects.get(produkt_id=request.POST.get('produkt_id'))
    product_to_restock = Produkty.objects.get(produkt_id=prod_id)
    form = ProduktyRestockForm(request.POST, instance=product_to_restock)
    if form.is_valid(): form.save()

    context = {
        'product': product_to_restock,
        'form': form
    }

    return render(request, "restock.html", context)

def add_product(request):
    form = ProduktyRemoveForm(request.POST)
    if form.is_valid():
        form.save()
        form = ProduktyRemoveForm() # clear form after submiting

    context ={
        "form": form
    }
    return render(request, "add_product.html", context)
