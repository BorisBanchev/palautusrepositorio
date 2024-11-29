class Summa:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
        self.edellinen_syote = -1

    def suorita(self):
        self.edellinen_syote = self.io.arvo()
        self.io.plus(self.syote())

    def kumoa(self):
        self.io.aseta_arvo(self.edellinen_syote)

class Erotus:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
        self.edellinen_syote = -1

    def suorita(self):
        self.edellinen_syote = self.io.arvo()
        self.io.miinus(self.syote())

    def kumoa(self):
        self.io.aseta_arvo(self.edellinen_syote)

class Nollaus:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote
        self.edellinen_syote = -1

    def suorita(self):
        self.edellinen_syote = self.io.arvo()
        self.io.nollaa()
    
    def kumoa(self):
        self.io.aseta_arvo(self.edellinen_syote)

class Kumoa:
    def __init__(self, io):
        self.io = io
        self.viimeisin_komento = -1
    
    def siirry_viimeiseen_komentoon(self, komento):
        self.viimeisin_komento = komento
    
    def suorita(self):
        if self.viimeisin_komento != -1:
            self.viimeisin_komento.kumoa()