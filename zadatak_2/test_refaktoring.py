from zadatak_2.refaktoring import Rezervacija, ServisRezervacija


# Zamjenski izvor podataka za testiranje
class LazniIzvor:
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj(self):
        return self.rezervacije


# Zamjenski izvjestaj za testiranje
class LazniIzvjestaj:
    def __init__(self):
        self.iznosi = []

    def posalji(self, iznosi):
        self.iznosi = iznosi.copy()


# Test 1: Provjera obracuna vise rezervacija
def test_obracun_rezervacija():
    podaci = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
    ]

    izvor = LazniIzvor(podaci)
    izvjestaj = LazniIzvjestaj()

    servis = ServisRezervacija(izvor, [izvjestaj])
    rezultat = servis.obradi()

    assert rezultat == [240, 325]
    assert izvjestaj.iznosi == [240, 325]


# Test 2: Provjera praznog izvora podataka
def test_prazne_rezervacije():
    izvor = LazniIzvor([])
    izvjestaj = LazniIzvjestaj()

    servis = ServisRezervacija(izvor, [izvjestaj])
    rezultat = servis.obradi()

    assert rezultat == []
    assert izvjestaj.iznosi == []


# Test 3: Provjera slanja na vise izvjestaja
def test_vise_izvjestaja():
    podaci = [Rezervacija("Ivana", 2, 120)]

    izvor = LazniIzvor(podaci)
    izvjestaj1 = LazniIzvjestaj()
    izvjestaj2 = LazniIzvjestaj()

    servis = ServisRezervacija(izvor, [izvjestaj1, izvjestaj2])

    rezultat = servis.obradi()

    assert rezultat == [240]
    assert izvjestaj1.iznosi == [240]
    assert izvjestaj2.iznosi == [240]
