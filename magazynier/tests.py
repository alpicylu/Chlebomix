from django.test import TestCase
from .models import Produkty
class ProduktyModelTest(TestCase):
    def setUp(self):
        self.produkt = Produkty.objects.create(nazwa_produktu='Produkt testowy')

    def test_nazwa_produktu(self):
        produkt = Produkty.objects.get(produkt_id=self.produkt.produkt_id)
        self.assertEqual(produkt.nazwa_produktu, 'Produkt testowy')

    def test_unikalnosci_produktu(self):
        with self.assertRaises(Exception) as context:
            Produkty.objects.create(nazwa_produktu='Produkt testowy')
        self.assertEqual(
            str(context.exception),
            'UNIQUE constraint failed: magazynier_produkty.nazwa_produktu'
        )

    def test_ilosc_dostepna(self):
        produkt = Produkty.objects.get(produkt_id=self.produkt.produkt_id)
        self.assertEqual(produkt.ilosc_dostepna, 0.0)