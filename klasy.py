
# Klasa = szablon, przepis
# Istota
# Zamysl
class Czlowiek:
    #Istota
    #atrybuty klasy
    gatunek = "Homo Sapiens"
    def __init__(self, imie): #atrybuty obiektu(skladniki potrawy)
        #Akt istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie} ")
        self.imie = imie

    def przedstaw_sie(self):
        print(f"Mam na imie {self.imie}")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

# Powstanie obiektuu
# Gotowanie z przepisu test

adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)

ewa.przedstaw_sie()
ewa.przedstaw(adam)
#print(type(adam))
#print(dir(adam))


#print(type(Czlowiek))
#print(dir(Czlowiek))


