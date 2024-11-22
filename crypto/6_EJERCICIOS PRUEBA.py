lista  = [1,5,2,7,9,32]

n = len(lista)

for posicion in range (n):

    for j in range (0, n - posicion - 1):
        if lista[j] < lista[j + 1]:
            lista [j], lista[j + 1] = lista [j + 1], lista [j]

print(lista)