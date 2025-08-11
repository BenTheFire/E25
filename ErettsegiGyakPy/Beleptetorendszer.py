class Esemeny:
    diak: str           # Example: "BZTU"
    idobelyeg: str      # Example: "14:10" [0:2] hour, [3:5] minute
    esemenytipus: int   # Types: 1 - In the gate, 2 - out the gate, 3 - meal, 4 - konyvtar

    def __init__(self, diak: str, idobelyeg: str, esemenytipus: int):
        self.diak = diak
        self.idobelyeg = idobelyeg
        self.esemenytipus = esemenytipus


print("1. Feladat.")
Esemenyek = []

with open("bedat.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        if len(parts) != 3:
            print(f"Hibás bemenet: {line.strip()}")
            raise ValueError("Hibás bemenet. Minden sornak meg kell felelnie: diak, idobelyeg, esemenytipus")  # Hibakezelés
        if not parts[2].isdigit():
            print(f"Hibás esemenytipus: {parts[2]}")
            raise ValueError("Hibás esemenytipus. Az esemenytipusnak egész számnak kell lennie")
        esemeny = Esemeny(parts[0], parts[1], int(parts[2]))
        Esemenyek.append(esemeny)

print(f"Összesen {len(Esemenyek)} esemény van a fájlban.")
for esemeny in Esemenyek:
    print(f"{esemeny.diak} {esemeny.idobelyeg} {esemeny.esemenytipus}")


print("\n2. Feladat.")