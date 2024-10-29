import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_pelaajien_hakeminen_palauttaa_oikean_maaran_pelaajia(self):
        pelaajat = self.stats._players
        self.assertAlmostEqual(len(pelaajat),5)
    
    def test_listalla_olevan_pelaajan_etsiminen_onnistuu(self):
        nimi = "Semenko"
        player = self.stats.search(nimi)
        self.assertEqual(player.name,nimi)
    
    def test_listalla_ei_olevan_pelaajan_etsiminen_palauttaa_none(self):
        nimi = "Boris"
        player = self.stats.search(nimi)
        self.assertEqual(player,None)

    def test_palauttaa_listan_jossa_vain_joukkueen_pelaajia(self):
        joukkue = self.stats.team("EDM")
        self.assertAlmostEqual(len(joukkue),3)
        
    def test_palauttaa_kärkipelaajat(self):
        top_players = self.stats.top(2)
        self.assertEqual(print(top_players),print([Player("Gretzky", "EDM", 35, 89),Player("Lemieux", "PIT", 45, 54),Player("Yzerman", "DET", 42, 56)]))

        

        

