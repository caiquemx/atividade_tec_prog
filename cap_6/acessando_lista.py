# cria uma lista de carros
carros = ['gol','fusca','palio','onix']

# acessa a lista
print(carros[0])
print(carros[1])

# muda o valor da posição 0
carros[0] = 'ferrari'
print(carros[0])


# Exemplo 2

lista = [10, 20, 30, 40, 50]

print(lista[0])

lista[0] = int(input('Digite um valor: '))
lista[1] = lista[0] + lista[2]

if(lista[1] > 5):
  print('Valor = ',lista[1])


# Exemplo 3

numeros = [1, 2, 3]

[x, y, z] = numeros

print(x)
print(y)
print(z)

#Exemplo 4

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acessa o primeiro item da primeira lista interna
print(lista_aninhada[0][0])

# Acessa o segundo item da segunda lista interna
print(lista_aninhada[1][1])

# Acessa o último item da última lista interna
print(lista_aninhada[2][2])