class Summa:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote

    def suorita(self):
        self.io.plus(self.syote())

class Erotus:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote

    def suorita(self):
        self.io.miinus(self.syote())

class Nollaus:
    def __init__(self, io, syote):
        self.io = io
        self.syote = syote

    def suorita(self):
        self.io.nollaa()