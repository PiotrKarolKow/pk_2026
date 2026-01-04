def zmien(a):
    a = 8
    return a
a=7
#argument jest przekazany jako kopia
a=zmien(a)
print(a)


def zmien_lista(lista):
    lista.append("hahaa")
    return lista
lista = [1,2]

zmien_lista(lista)
print(lista)