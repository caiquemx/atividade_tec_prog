lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# adiciona uma nova lista ao final
lista_aninhada.append([10, 11, 12])
print(lista_aninhada)

# Altera o primeiro item da primeira lista interna
lista_aninhada[0][0] = 'python'
print(lista_aninhada)



## Iterando

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Percorre apenas os elementos
for lista in lista_aninhada:
  for item in lista:
    print(item)

# Percorre os índices e elementos
for y in range(len(lista_aninhada)):
  for x in range(len(lista_aninhada[y])):
    print(y,x,lista_aninhada[y][x])