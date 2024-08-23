lista = [1, 2, 3, 4, 5, 6]

# remove o elemento da posição 0
del lista[0]
print(lista)

# remove os elementos das posições 0 e 1
del lista[:2]
print(lista)

## removendo elementos de lista aninhadas

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# remove o elemento da posição 0 da lista 0
del lista_aninhada[0][0]
print(lista_aninhada)

# remove toda a lista da posição 1
del lista_aninhada[1]
print(lista_aninhada)