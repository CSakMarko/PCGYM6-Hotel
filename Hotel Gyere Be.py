#Absztrakt osztályok
from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
    
    @abstractmethod
    def foglalasi_ar(self):
        pass

#Egy kétágyas osztályok
class EgyagyasSzoba(Szoba):
    def foglalasi_ar(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, extra_dij):
        super().__init__(ar, szobaszam)
        self.extra_dij = extra_dij
    
    def foglalasi_ar(self):
        return self.ar + self.extra_dij

#Szálloda osztályok
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
    
    def add_szoba(self, szoba):
        self.szobak.append(szoba)

#Foglalás osztály
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

#Foglalások kezelése
class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok = []
    
    def foglalas(self, szoba, datum):
        uj_foglalas = Foglalas(szoba, datum)
        self.foglalasok.append(uj_foglalas)
        return szoba.foglalasi_ar()
    
    def lemondas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False
    
    def listazas(self):
        return self.foglalasok

#Felhaszn interf.
def main():
    szalloda = Szalloda("Hotel Gyere be")
    rendszer = FoglalasiRendszer()
    
    szoba1 = EgyagyasSzoba(10000, 101)
    szoba2 = KetagyasSzoba(15000, 102, 5000)
    
    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    
    while True:
        print("\n1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Összes foglalás listázása")
        print("4. Kilépés")
        
        valasztas = input("Válassz egy opciót: ")
        
        if valasztas == '1':
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum = input("Add meg a dátumot (YYYY-MM-DD): ")
            szoba = next((sz for sz in szalloda.szobak if sz.szobaszam == szobaszam), None)
            if szoba:
                ar = rendszer.foglalas(szoba, datum)
                print(f"Foglalás sikeres! Ár: {ar} Ft")
            else:
                print("Szoba nem található!")
        
        elif valasztas == '2':
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum = input("Add meg a dátumot (YYYY-MM-DD): ")
            szoba = next((sz for sz in szalloda.szobak if sz.szobaszam == szobaszam), None)
            if szoba and rendszer.lemondas(szoba, datum):
                print("Foglalás lemondva!")
            else:
                print("Foglalás nem található!")
        
        elif valasztas == '3':
            foglalasok = rendszer.listazas()
            if foglalasok:
                for foglalas in foglalasok:
                    print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")
            else:
                print("Nincs foglalás!")
        
        elif valasztas == '4':
            break
        
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()