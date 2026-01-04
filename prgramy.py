class Zloty(float):
    def __add__(self, other):
        super().__add__(other)
        return Zloty(super().__add__(other))

    def zmien_na_euro(self):
        return self/4.21

a = Zloty(4)
b = Zloty(7)
c = Zloty(a+b)
c.zmien_na_euro()

print(a + b)
print(c)
print(c.zmien_na_euro())
print(type(c.zmien_na_euro()))

class WebDriver:
    #Klasa nadrzedna - sterownik przegladarki
    def maximize_window(self):
    pass

class Firefox(WebDriver):
    def maximize_window(self):

class Google