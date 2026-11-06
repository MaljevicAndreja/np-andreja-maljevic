import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


# Podaci o jednoj rezervaciji
@dataclass
class Rezervacija:
    gost: str
    noci: int
    cijena_noci: float


# Protocol za izvor podataka
class IzvorPodataka(Protocol):
    def ucitaj(self) -> list[Rezervacija]: ...


# Protocol za izvjestavanje
class Izvjestavanje(Protocol):
    def posalji(self, iznosi: list[float]) -> None: ...


# Klasa koja cita rezervacije iz CSV datoteke
class CsvIzvor:
    def __init__(self, putanja: Path):
        self.putanja = putanja

    def ucitaj(self) -> list[Rezervacija]:
        rezervacije = []

        with self.putanja.open(encoding="utf-8-sig", newline="") as f:
            for red in csv.DictReader(f):
                rezervacije.append(
                    Rezervacija(
                        gost=red["gost"],
                        noci=int(red["noci"]),
                        cijena_noci=float(red["cijena_noci"]),
                    )
                )

        return rezervacije


# Klasa koja racuna iznos rezervacije
class ObracunRezervacija:
    def izracunaj(self, r: Rezervacija) -> float:
        return r.noci * r.cijena_noci


# Klasa koja cuva izvjestaj u datoteku
class TekstualniIzvjestaj:
    def __init__(self, putanja: Path):
        self.putanja = putanja

    def posalji(self, iznosi: list[float]) -> None:
        self.putanja.write_text(str(iznosi), encoding="utf-8")


# Klasa koja simulira slanje obavjestenja
class Obavjestenje:
    def posalji(self, iznosi: list[float]) -> None:
        print("Poslato:", sum(iznosi))


# Glavni servis za obradu rezervacija
class ServisRezervacija:
    def __init__(
        self,
        izvor: IzvorPodataka,
        izvjestaji: list[Izvjestavanje],
    ):
        self.izvor = izvor
        self.izvjestaji = izvjestaji
        self.obracun = ObracunRezervacija()

    def obradi(self) -> list[float]:
        rezervacije = self.izvor.ucitaj()

        iznosi = [self.obracun.izracunaj(r) for r in rezervacije]

        for izvjestaj in self.izvjestaji:
            izvjestaj.posalji(iznosi)

        return iznosi


if __name__ == "__main__":
    folder = Path(__file__).parent

    izvor = CsvIzvor(folder.parent / "rezervacije.csv")

    servis = ServisRezervacija(
        izvor,
        [
            TekstualniIzvjestaj(folder / "izvjestaj.txt"),
            Obavjestenje(),
        ],
    )

    servis.obradi()
