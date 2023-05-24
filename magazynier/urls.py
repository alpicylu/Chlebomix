from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_storage, name="magazyn"),
    path('uzupelnij/<int:prod_id>', views.restock_form, name="uzupelnij"),
    path('dodaj/', views.add_product, name="dodaj")
]
