# np-andreja-maljevic
# Napredno programiranje – Zadatak 1

**Ime i prezime:** Andreja Maljević  
**Broj indeksa:** 26/006  
**Predmet:** Napredno programiranje  
**Fakultet:** FIST, Univerzitet Donja Gorica

## Opis zadatka

U ovom zadatku trebalo je da pripremimo radno okruženje za Python, napravimo GitHub repozitorijum i uz pomoć AI asistenta napišemo funkciju koja računa prosječnu cijenu noćenja na osnovu podataka iz CSV datoteke.

Za rad sam koristila Python 3.13.3, VS Code, GitHub, Ruff, pytest i ChatGPT.

## Python program

Napravila sam funkciju `prosjecna_cijena` koja učitava podatke iz datoteke `rezervacije.csv`.

Podaci sadrže ime gosta, broj noćenja i cijenu jednog noćenja.

Program računa ukupan iznos svih rezervacija i dijeli ga ukupnim brojem noćenja.

Za podatke koje sam koristila dobila sam prosječnu cijenu od **80.50 EUR**.

## Korišćenje AI asistenta

Tokom rada koristila sam ChatGPT kao pomoć pri pisanju i provjeri koda.

Neki od upita koje sam koristila su:

- „Zašto ne mogu samo Run da koristim i da je kod direktno povezan sa CSV?”
- „Daj cijeli kod.”
- „Makni samo koje kolone Python vidi.”

AI mi je pomogao da napišem funkciju, povežem je sa CSV datotekom i pronađem greške tokom pokretanja programa.

## Uočeni problemi i nedostaci

Tokom rada naišla sam na nekoliko problema:

- Na početku sam dobila grešku `KeyError: 'noci'`, jer Python nije pravilno prepoznavao kolone iz CSV datoteke.
- Dodala sam provjeru naziva kolona kako bih pronašla problem, a kasnije sam uklonila taj ispis.
- Prvobitni kod nije imao posebno obrađene sve moguće greške, kao što su nedostajuće kolone i negativne vrijednosti.
- Funkcija prijavljuje grešku ako nema ostvarenih noćenja ili ako neki numerički podatak nije ispravan.

Ovo mi je pokazalo da kod koji generiše AI treba pokrenuti i provjeriti, a ne samo kopirati.

## Testiranje

Napravila sam tri testa pomoću pytesta:

1. Test pravilnog izračunavanja prosječne cijene.
2. Test prazne CSV datoteke.
3. Test neispravnih podataka.

Sva tri testa su uspješno prošla (**3 passed**).

Takođe sam koristila Ruff za provjeru i formatiranje koda. Nakon formatiranja sve provjere su uspješno završene.

## Zaključak

Kroz ovaj zadatak sam vježbala rad sa Python funkcijama, CSV datotekama, GitHubom i alatima za testiranje.

Koristila sam AI kao pomoć pri pisanju koda, ali sam kroz pokretanje programa i testove provjerila da li rješenje radi kako treba.