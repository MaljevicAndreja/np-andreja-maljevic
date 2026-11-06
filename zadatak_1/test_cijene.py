from pathlib import Path

import pytest

from cijene import prosjecna_cijena


# TEST 1: Provjera ispravnog izracunavanja prosjeka
def test_prosjecna_cijena(tmp_path: Path) -> None:
    datoteka = tmp_path / "rezervacije.csv"

    datoteka.write_text(
        "gost,noci,cijena_noci\nAna,3,80\nMarko,5,65\nIvana,2,120\n",
        encoding="utf-8",
    )

    assert prosjecna_cijena(datoteka) == 80.5


# TEST 2: Provjera prazne CSV datoteke
def test_prazna_datoteka(tmp_path: Path) -> None:
    datoteka = tmp_path / "prazna.csv"

    datoteka.write_text(
        "gost,noci,cijena_noci\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        prosjecna_cijena(datoteka)


# TEST 3: Provjera neispravnih podataka
def test_neispravni_podaci(tmp_path: Path) -> None:
    datoteka = tmp_path / "neispravna.csv"

    datoteka.write_text(
        "gost,noci,cijena_noci\nAna,abc,80\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        prosjecna_cijena(datoteka)
