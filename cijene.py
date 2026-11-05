import csv
from pathlib import Path


def prosjecna_cijena(putanja: Path) -> float:

    ukupno = 0.0
    ukupno_noci = 0

    with putanja.open(newline="", encoding="utf-8-sig") as f:
        citac = csv.DictReader(f)

        for red in citac:
            noci = int(red["noci"])
            cijena_noci = float(red["cijena_noci"])

            ukupno += noci * cijena_noci
            ukupno_noci += noci

    if ukupno_noci == 0:
        raise ValueError("Nema ostvarenih nocenja")

    return ukupno / ukupno_noci


if __name__ == "__main__":
    putanja = Path(__file__).with_name("rezervacije.csv")

    rezultat = prosjecna_cijena(putanja)

    print(f"Prosjecna cijena nocenja: {rezultat:.2f} EUR")
