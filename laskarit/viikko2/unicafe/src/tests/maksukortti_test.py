import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(511)
        self.assertEqual(1511, self.maksukortti.saldo)

    def test_otettaessa_rahaa_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(750, self.maksukortti.saldo)

    def test_otettaessa_liikaa_rahaa_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1250)
        self.assertEqual(1000, self.maksukortti.saldo)

    def test_ottometodi_palauttaa_onnistumisstatuksen(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1250))
        self.assertTrue(self.maksukortti.ota_rahaa(250))

    def test_saldo_euroina_oikein(self):
        self.maksukortti.saldo = 1050
        self.assertEqual(10.5, self.maksukortti.saldo_euroina())

    def test_oikea_merkkijonoesitys(self):
        self.maksukortti.saldo = 1050
        self.assertEqual("Kortilla on rahaa 10.50 euroa", str(self.maksukortti))
