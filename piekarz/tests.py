from django.test import TestCase
from .models import Przepisy, Skladniki, Produkty
from django.db.utils import IntegrityError

class PrzepisyModelTest(TestCase):
    def setUp(self):
        self.przepis = Przepisy.objects.create(nazwa_przepisu='Przepis testowy')

    def test_nazwa_przepisu(self):
        przepis = Przepisy.objects.get(przepis_id=self.przepis.przepis_id)
        self.assertEqual(przepis.nazwa_przepisu, 'Przepis testowy')

class SkladnikiModelTest(TestCase):
    def setUp(self):
        self.przepis = Przepisy.objects.create(nazwa_przepisu='Przepis testowy')
        self.produkt = Produkty.objects.create(nazwa_produktu='Produkt testowy')
        Produkty.objects.create(nazwa_produktu='Produkt testowy 2')

        self.skladnik = Skladniki.objects.create(przepis_id=self.przepis.przepis_id, produkt_id=1, ilosc_produktu=10.5)
        Skladniki.objects.create(przepis_id=self.przepis.przepis_id, produkt_id=2, ilosc_produktu=5.0)

    def test_unikalnosci_przepisu(self):
        with self.assertRaises(Exception) as context:
            Przepisy.objects.create(nazwa_przepisu='Przepis testowy')
        self.assertEqual(
            str(context.exception),
            'UNIQUE constraint failed: piekarz_przepisy.nazwa_przepisu'
        )

    def test_unikalnosci_skladnika(self):
        with self.assertRaises(Exception) as context:
            Skladniki.objects.create(przepis_id=1, produkt_id=1, ilosc_produktu=69.5)
        self.assertEqual(
            str(context.exception),
            'UNIQUE constraint failed: piekarz_skladniki.przepis_id, piekarz_skladniki.produkt_id'
        )

    def test_przepis_id(self):
        skladnik = Skladniki.objects.get(krotka_id=self.skladnik.krotka_id)
        self.assertEqual(skladnik.przepis_id, 1)

    def test_nazwy_produktu_w_skladniku(self):
        skladnik = Skladniki.objects.get(krotka_id=self.skladnik.krotka_id)
        self.assertEqual(Produkty.objects.get(produkt_id=skladnik.produkt_id).nazwa_produktu,  'Produkt testowy')

    def test_produkt_id(self):
        skladnik = Skladniki.objects.get(krotka_id=self.skladnik.krotka_id)
        self.assertEqual(skladnik.produkt_id, 1)

    def test_ilosc_produktu(self):
        skladnik = Skladniki.objects.get(krotka_id=self.skladnik.krotka_id)
        self.assertEqual(skladnik.ilosc_produktu, 10.5)

    def test_typ_pola_nazwa_przepisu(self):
        przepis = Przepisy.objects.create(nazwa_przepisu='Przepis testowy jakis')
        self.assertIsInstance(przepis.nazwa_przepisu, str)

    def test_typ_pola_ilosc_produktu(self):
        skladnik = Skladniki.objects.get(krotka_id=self.skladnik.krotka_id)
        self.assertIsInstance(skladnik.ilosc_produktu, float)

    def test_usuniecie_przepisu_usuwa_skladniki(self):
        self.assertEqual(Przepisy.objects.count(), 1)
        self.assertEqual(Skladniki.objects.count(), 2)
        self.przepis.delete()
        self.assertEqual(Przepisy.objects.count(), 0)
        self.assertEqual(Skladniki.objects.count(), 0)