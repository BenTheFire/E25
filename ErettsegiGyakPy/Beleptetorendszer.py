# Hozzunk létre egy globális listát, amelyben az eseményeket tároljuk
Esemenyek = []

# Hozzunk létre egy szótárat, amely az eseménytípusokat reprezentálja
# > C nyelvekben ez ENUM lenne. Pythonban a szótár egy jó alternatíva
# > Későbbi tanulmányok során az ENUM és a dataclass használata profibb és preferált megoldás lesz
esemenytar = {
    1: "Belépett az iskolába",
    2: "Kilépett az iskolából",
    3: "Átvette az ebédet az étkezőben",
    4: "Kikölcsönzött egy könyvet a könyvtárból"
}


# Hozzunk létre egy függvényt, amely visszaadja az esemény reprezentációját
def esemeny_rep(esemenyazon):
    """Visszaadja az esemény reprezentációját."""
    return esemenytar[esemenyazon]


'------ Osztályok -------'


# Hozzunk létre egy osztályt, amely az eseményeket reprezentálja -> Osztály = Objektum Reprezentáció
class Esemeny:
    """
    Esemény osztály, amely egy diák eseményét reprezentálja.

    Attributes:
    ----------
    diak: str           # Diák azonosítója, például "BZTU"
    idobelyeg: str      # Időbélyeg, például "14:10" (0-2 óra, 3-5 perc)
    esemenytipus: int   # Eseménytípus: 1 - Be a kapuba, 2 - Ki a kapuból, 3 - Étkezés, 4 - Könyvtár
    """
    diak: str  # Example: "BZTU"
    idobelyeg: str  # Example: "14:10" [0:2] hour, [3:5] minute
    esemenytipus: int  # Types: 1 - In the gate, 2 - out the gate, 3 - meal, 4 - konyvtar

    # Inicializáló metódus, konstruktor, vagy példányosító metódus
    # > Feladatai: Létrehozza az objektumot, beállítja az attribútumokat, egyéb kezdeti kezelések, pl. logging
    # > Használata: ClassNeve(param1, param2, ...)
    def __init__(self, diak: str, idobelyeg: str, esemenytipus: int):
        self.diak = diak
        self.idobelyeg = idobelyeg
        self.esemenytipus = esemenytipus

    # String reprezentáció, amelyet a print függvény hív meg
    # > Mit csinál? -> Visszaadja az objektum szöveges reprezentációját
    def __str__(self):
        return f"{self.diak} kódú diák {self.idobelyeg} időpontban {esemeny_rep(self.esemenytipus)}."

    # Repr reprezentáció, amelyet a repr függvény hív meg
    # > Mit csinál? -> Visszaadja az objektum részletesebb reprezentációját, általában a fejlesztéshez hasznos
    def __repr__(self):
        return f"{self.diak} {self.idobelyeg} {self.esemenytipus} ({esemeny_rep(self.esemenytipus)})"

    # Segédfüggvény, amely visszaadja az időbélyeget percben
    def percben(self):
        return idobelyeg_percben(self.idobelyeg)


'------- Segédfüggvények -------'


def diak_esmenyei(diak_kod):
    """Visszaadja a megadott diák eseményeit."""
    diak_esemenyek = []
    for esemeny in Esemenyek:
        if esemeny.diak == diak_kod:
            diak_esemenyek.append(esemeny)
    return diak_esemenyek


def idobelyeg_percben(idobelyeg):
    """Visszaadja az időbélyeget percekben."""
    ora = int(idobelyeg[0:2])  # Az első két karakter az óra
    perc = int(idobelyeg[3:5])  # A harmadik és negyedik karakter a perc
    return ora * 60 + perc


'------- Feladatok -------'

print("1. Feladat.")
with open("bedat.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        if len(parts) != 3:
            print(f"Hibás bemenet: {line.strip()}")
            raise ValueError(
                "Hibás bemenet. Minden sornak meg kell felelnie: diak, idobelyeg, esemenytipus")  # Hibakezelés
        if not parts[2].isdigit():
            print(f"Hibás esemenytipus: {parts[2]}")
            raise ValueError("Hibás esemenytipus. Az esemenytipusnak egész számnak kell lennie")
        esemeny = Esemeny(parts[0], parts[1], int(parts[2]))
        Esemenyek.append(esemeny)

print(f"Összesen {len(Esemenyek)} esemény van a fájlban.")
for esemeny in Esemenyek:
    print(f"{esemeny.diak} {esemeny.idobelyeg} {esemeny.esemenytipus}")

print("\n2. Feladat, Első és Utolsó")
"""
Jegyzet - Átalakítás, pivot, felhasználás

Jelenlegi formátum:
Esemenyek[0].diak, Esemenyek[0].idobelyeg, Esemenyek[0].esemenytipus
Esemenyek[1].diak, Esemenyek[1].idobelyeg, Esemenyek[1].esemenytipus
...
Esemenyek[n].diak, Esemenyek[n].idobelyeg, Esemenyek[n].esemenytipus (ahol n a sorok száma) 


Kívánt formátum:
Diák - Események (EsemenyLista)
Diák2 - Események2
...
DiákN - EseményekN (ahol N a diákok száma)

Írjunk egy függvényt, amely átalakítja a jelenlegi formátumot a kívánt formátumra.

Ezen kívül, írjunk egy függvényt ami az időbélyeget visszaadja percben.
"""
elso_belepes = None
utolso_kilepes = None
for esemeny in Esemenyek:
    if esemeny.esemenytipus == 1:  # Be a kapuba
        if elso_belepes is None or esemeny.percben() < elso_belepes.percben():
            elso_belepes = esemeny
    elif esemeny.esemenytipus == 2:  # Ki a kapuból
        if utolso_kilepes is None or esemeny.percben() > utolso_kilepes.percben():
            utolso_kilepes = esemeny

print(f"Az első tanuló {elso_belepes.idobelyeg}-kor lépett be a főkapun.\n"
      f"Az utolsó tanuló {utolso_kilepes.idobelyeg}-kor lépett ki a főkapun.")  # szeginy tulorazott

print("\n3. Feladat, Késők")
kesok = []
for esemeny in Esemenyek:
    if esemeny.esemenytipus == 1:  # Be a kapuba
        if esemeny.percben() in range(idobelyeg_percben("07:51"), idobelyeg_percben("08:15")):
            # Ha a belépés később van, mint 7:50, de korábban, mint 8:15
            kesok.append(esemeny)
with open("kesok.txt", "w") as file:  # w - write, felülírja (törli az eredeti) a fájlt (ha létezik), ha nem, akkor létrehozza
    for keso in kesok:
        file.write(f"{keso.diak} {keso.idobelyeg}\n")

