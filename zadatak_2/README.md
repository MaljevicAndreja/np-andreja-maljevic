# Zadatak 2 – OOP i SOLID principi

**Ime i prezime:** Andreja Maljević  
**Broj indeksa:** 26/006  
**Predmet:** Napredno programiranje  
**Fakultet:** FIST, Univerzitet Donja Gorica

## Opis zadatka

U ovom zadatku trebalo je da poboljšam postojeći Python kod za obradu rezervacija primjenom SOLID principa.

Početni kod je bio u datoteci `obrada.py`, a poboljšanu verziju sam napravila u `refaktoring.py`.

Za rad sam koristila Python, VS Code, ChatGPT, pytest i Ruff.

## Šta sam uradila

U početnom kodu jedna klasa je obavljala više poslova: učitavanje rezervacija, računanje iznosa, čuvanje izvještaja i slanje obavještenja.

Kod sam podijelila na nekoliko klasa kako bi svaka imala svoj zadatak.

Primijenila sam dva SOLID principa:

- **S (Single Responsibility)** – razdvojila sam odgovornosti u posebne klase.
- **D (Dependency Inversion)** – koristila sam `Protocol` za izvor podataka i izvještavanje.

Napravila sam i zamjenske klase za testiranje, tako da program možemo provjeriti bez korišćenja stvarne CSV datoteke.

## Korišćenje AI asistenta

Tokom izrade zadatka koristila sam ChatGPT za pomoć pri pisanju i objašnjavanju koda.

Neki od upita koje sam koristila su:

- „Hajde da radimo zadatak za 4 boda redom, korak po korak.”
- „Hajde dalje.”

Takođe sam AI asistentu slala rezultate testiranja i Ruff provjera kako bih dobila objašnjenja i potrebne ispravke.

## Uočeni problemi i ispravke

Tokom rada uočila sam nekoliko nedostataka početnog koda:

1. Jedna klasa je radila više različitih poslova. To sam riješila razdvajanjem na posebne klase.
2. Početni kod je direktno zavisio od datoteke. U novoj verziji sam dodala `Protocol` kako bi se mogli koristiti različiti izvori podataka.
3. Za rad sa datotekama korišćen je `open()` bez `with`. U poboljšanoj verziji datoteke se pravilno otvaraju i zatvaraju.
4. Prilikom Ruff provjere novog koda bilo je potrebno popraviti formatiranje. Koristila sam `ruff format` i nakon toga ponovo pokrenula testove.

Originalni kod sam ostavila u `obrada.py` radi poređenja.

## Testiranje

Napravila sam tri testa u datoteci `test_refaktoring.py`:

1. Provjera pravilnog obračuna rezervacija.
2. Provjera rada programa kada nema rezervacija.
3. Provjera slanja rezultata na više izvještaja.

Testove sam pokrenula komandom:

`python -m pytest zadatak_2/test_refaktoring.py -v`

**Rezultat: 3 passed.**

Kod sam provjerila i pomoću Ruffa. Sve provjere novog koda su uspješno završene.

## Zaključak

Kroz ovaj zadatak sam vježbala objektno orijentisano programiranje i SOLID principe.

Naučila sam kako da podijelim kod na više klasa i kako da koristim `Protocol` za jednostavnije testiranje i izmjene programa.

AI mi je pomogao pri izradi zadatka, a ispravnost koda sam provjerila pokretanjem programa i automatskim testovima.