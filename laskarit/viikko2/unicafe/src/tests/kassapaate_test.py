import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikein_luotu(self):
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)
        self.assertEqual(0, self.kassapaate.edulliset)
        self.assertEqual(0, self.kassapaate.maukkaat)

    def test_onnistunut_osto_edullinen_vaihtoraha_oikein(self):
        self.assertEqual(123, self.kassapaate.syo_edullisesti_kateisella(240 + 123))

    def test_onnistunut_osto_edullinen_kassan_rahamaara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(100000 + 240, self.kassapaate.kassassa_rahaa)

    def test_onnistunut_osto_edullinen_myytyjen_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(1, self.kassapaate.edulliset)

    def test_onnistunut_osto_maukas_vaihtoraha_oikein(self):
        self.assertEqual(123, self.kassapaate.syo_maukkaasti_kateisella(400 + 123))

    def test_onnistunut_osto_maukas_kassan_rahamaara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(100000 + 400, self.kassapaate.kassassa_rahaa)

    def test_onnistunut_osto_maukas_myytyjen_lounaiden_maara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(1, self.kassapaate.maukkaat)

    def test_epaonnistunut_osto_maukas(self):
        self.assertEqual(399, self.kassapaate.syo_maukkaasti_kateisella(399))
        self.assertEqual(0, self.kassapaate.maukkaat)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_epaonnistunut_osto_edullinen(self):
        self.assertEqual(239, self.kassapaate.syo_edullisesti_kateisella(239))
        self.assertEqual(0, self.kassapaate.edulliset)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_onnistunut_korttiosto_edullinen_veloitus_oikein(self):
        kortti = Maksukortti(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(0, kortti.saldo)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)
        self.assertEqual(1, self.kassapaate.edulliset)

    def test_onnistunut_korttiosto_maukas_veloitus_oikein(self):
        kortti = Maksukortti(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(0, kortti.saldo)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)
        self.assertEqual(1, self.kassapaate.maukkaat)

    def test_epaonnistunut_korttiosto_edullinen(self):
        kortti = Maksukortti(239)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(239, kortti.saldo)
        self.assertEqual(0, self.kassapaate.edulliset)

    def test_epaonnistunut_korttiosto_maukas(self):
        kortti = Maksukortti(239)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(239, kortti.saldo)
        self.assertEqual(0, self.kassapaate.maukkaat)

    def test_kortti_latautuu_oikein(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(150, kortti.saldo)
        self.assertEqual(100050, self.kassapaate.kassassa_rahaa)

    def test_negatiivinen_kortin_lataus_ei_tee_mitaan(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -50)
        self.assertEqual(100, kortti.saldo)
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)

    def test_kassan_rahamaara_euroina(self):
        self.assertEqual(1000.0, self.kassapaate.kassassa_rahaa_euroina())
