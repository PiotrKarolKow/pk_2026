# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()
import math


# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie

class FiguraGeometryczna():

    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def policz_pole(self):
        return self.a * self.b
    def policz_obwod(self):
        return 2 * (self.a + self.b)

class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        self.a = a
    def policzpole_kwadratu(self):
        return self.a * self.a

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r
    def policz_pole_kola(self):
        return math.pi * self.r ** 2

class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def policz_pole(self):
        return (self.a * self.h) / 2
    def policz_obwod(self):
        return self.a + self.b + self.c

trojkat = Trojkat(2,4,5,8)
trojkat_obwod = trojkat.policz_obwod()
torjkat_pole = trojkat.policz_pole()
print("To obowd trojkata:",trojkat_obwod)
print("To pole trojkata:",torjkat_pole)

kolo = Kolo(5)
prostokat = Prostokat(15, 6)
kwadrat = Kwadrat(5)


kwadrat = kwadrat.policzpole_kwadratu()
figura = prostokat.policz_obwod()
figurka= prostokat.policz_pole()
kolo = kolo.policz_pole_kola()

print("To obowod prostokata",figura)
print("To pole prostokata",figurka)
print("To pole kola",kolo)
print("To pole kwadratu",kwadrat)
# print("To obwod kwadratu", kwadrat.policz_obwod())
