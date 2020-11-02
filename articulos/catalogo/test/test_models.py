from django.test import TestCase
from models import Producto

class ProdTestCase(TestCase):
    def setUp(self):
        p1=Producto.objects.create(nom="Tazón")
        p2=Producto.objects.create(nom="Llavero")
        Producto.objects.create(id="T3", nom=p1, summary="Tazón mágico")
        Producto.objects.create(id="L2", nom=p2, summary="Llavero corazón")

def test_Prod_data(self):
    produ1 = Producto.objects.get(id="T3")
    self.assertEqual(produ1.Producto.nom, "Tazón")
    