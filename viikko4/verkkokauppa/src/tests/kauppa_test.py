import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 0
            
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else 0

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")


        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_asioinnin_paatyttya_pankin_metodia_tilimaksu_kutsutaan_oikeilla_argumenteilla(self):

        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 0
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else 0
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote



        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",5)

    def test_asionnin_paatyttya_korissa_kaksi_eri_tuotetta_ja_pankin_metodia_tilisiirto_kutsutaan_oikein(self):

        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 10
            
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else  Tuote(2, "leipä", 5)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.varasto_mock.hae_tuote.assert_called_with(2)
        self.kauppa.tilimaksu("pekka", "12345")

        
        

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",10)

    def test_asionnin_paatyttya_korissa_kaksi_samaa_tuotetta_jota_on_varastossa_ja_pankin_metodia_tilisiirto_kutsutaan_oikein(self):

        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 10
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else  Tuote(2, "leipä", 5)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",10)

    def test_asioinnin_paatyttya_korissa_tuote_jota_on_ja_tuote_jota_ei_ole_niin_kutsutaan_tilisiirtoa_oikein(self):

        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 0
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else  Tuote(2, "leipä", 5)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.kauppa.tilimaksu("pekka", "12345")

        

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",5)

    def test_aloita_asionti_metodin_kutsuminen_nollaa_edellisen_ostoksen_tiedot(self):
        
        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 10
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else  Tuote(2, "leipä", 5)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote



        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.varasto_mock.hae_tuote.assert_called_with(2)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.varasto_mock.hae_tuote.assert_called_with(2)
        self.kauppa.tilimaksu("pekka", "12345")

        


        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",5)
    
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42,43]

        def varasto_saldo(tuote_id):
            return 10 if tuote_id == 1 else 10
            
        def varasto_hae_tuote(tuote_id):
            return Tuote(1, "maito", 5) if tuote_id == 1 else  Tuote(2, "leipä", 5)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.saldo.assert_called_with(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.varasto_mock.hae_tuote.assert_called_with(2)

        self.kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345", "33333-44455",10)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.varasto_mock.saldo.assert_called_with(2)
        self.varasto_mock.hae_tuote.assert_called_with(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",43,"12345", "33333-44455",5)
    
    


        