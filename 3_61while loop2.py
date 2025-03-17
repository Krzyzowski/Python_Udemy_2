
lista = ["Ania", "Ola", "Kasia", "Daniel"]

nowaLista = []

k = len(lista) - 1

while k >= 0:
    nowaLista.append(lista[k])
    k -= 1

print("nowa lista", nowaLista)