
KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or not isinstance(kasvatuskoko, int):
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava kokonaislukuja")

        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava epänegatiivisia")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.luku_lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.luku_lista
        

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.luku_lista[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.luku_lista):
                taulukko_old = self.luku_lista
                self.luku_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.luku_lista)


    def poista(self, n):
        try:
            self.luku_lista.remove(n)
            self.alkioiden_lkm -= 1
        
        except:
            return

    def kopioi_lista(self, a, b):
        b[:len(a)] = a

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.luku_lista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_lista = IntJoukko()
        eka_lista = a.to_int_list()
        toka_lista = b.to_int_list()

        for luku in eka_lista + toka_lista:
            yhdiste_lista.lisaa(luku)

        return yhdiste_lista

    @staticmethod
    def leikkaus(a, b):
        leikkaus_lista = IntJoukko()
        eka_lista = a.to_int_list()
        toka_lista = b.to_int_list()

        for luku in eka_lista:
            if luku in toka_lista:
                leikkaus_lista.lisaa(luku)
        
        return leikkaus_lista

    @staticmethod
    def erotus(a, b):
        erotus_lista = IntJoukko()
        eka_lista = a.to_int_list()
        toka_lista = b.to_int_list()

        for luku in eka_lista:
            if luku not in toka_lista:
                erotus_lista.lisaa(luku)
        
        return erotus_lista

        

    def __str__(self):
        return f"{'{'}{', '.join(map(str, self.luku_lista[:self.alkioiden_lkm]))}{'}'}"
