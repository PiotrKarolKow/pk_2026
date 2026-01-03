
# Klasa = szablon, przepis
# Istota
# Zamysl
class Czlowiek:
    #Istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        #Akt istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie} ")
        self.imie = imie

# Powstanie obiektuu
# Gotowanie z przepisu test

adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)

#print(type(adam))
#print(dir(adam))


#print(type(Czlowiek))
#print(dir(Czlowiek))


