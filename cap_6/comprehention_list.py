## Quadrados dos números

numeros = [1, 2, 3, 4, 5]

# usando um comando de repetição
quadrados = []
for x in numeros:
  quadrados.append(x ** 2)
  print(quadrados)

# usando compreensão de lista
quadrados = [x ** 2 for x in numeros]
print(quadrados)


## Selecionando elementos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# usando um comando de repetição
pares = []
for x in numeros:
  if(x % 2 == 0):
    pares.append(x)
    print(pares)
    
# usando compreensão de lista
pares = [x for x in numeros if x % 2 == 0]
print(pares)