# Listas em Python
# ----------------

# Em Python, as listas funcionam de maneira semelhante a vetores ou matrizes (arrays) em outras linguagens,
# com a vantagem de serem dinâmicas e capazes de armazenar diferentes tipos de dados.

# Características das Listas:
# - Dinâmicas: Não possuem tamanho fixo; podem crescer e encolher conforme necessário.
# - Diversificadas: Podem armazenar qualquer tipo de dado: int, float, string, bool, etc.

# Representação de Listas:
# As listas em Python são representadas por colchetes: []

# Exemplos de Listas:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []  # Lista vazia
lista4 = list(range(1, 11))  # Lista com números de 1 a 10
lista5 = list('Geek University')  # Lista com cada caractere como um elemento

# Verificando a Presença de Elementos:
# ------------------------------------
# Podemos verificar se um determinado valor está presente na lista usando o operador 'in'.
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

# Ordenando Listas:
# -----------------
# A função sort() ordena os elementos da lista in-place.
lista1.sort()
print(lista1)  # Saída: [1, 1, 3, 4, 15, 22, 27, 27, 42, 44, 99]

# Contando Ocorrências de Elementos:
# ----------------------------------
# O método count() conta o número de ocorrências de um valor na lista.
print(lista1.count(1))  # Saída: 2
print(lista5.count('e'))  # Saída: 3

# Adicionando Elementos:
# ----------------------
# Método append(): Adiciona um elemento no final da lista.
lista1.append(42)
print(lista1)

# Método extend(): Adiciona todos os elementos de outra lista no final da lista.
lista1.extend([123, 44, 67])
print(lista1)

# Método insert(): Insere um elemento em uma posição específica.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Combinando Listas:
# -------------------
# Podemos combinar duas listas usando o operador +.
lista6 = lista1 + lista2
print(lista6)

# Invertendo Listas:
# ------------------
# Método reverse(): Inverte a ordem dos elementos in-place.
lista1.reverse()
print(lista1)

# Slicing: Também podemos inverter uma lista usando slicing.
print(lista1[::-1])

# Copiando Listas:
# ----------------
# Método copy(): Cria uma cópia da lista.
lista6 = lista2.copy()
print(lista6)

# Obtendo o Tamanho da Lista:
# ---------------------------
# A função len() retorna o número de elementos na lista.
print(len(lista5))  # Saída: 14

# Podemos remover facilmente o último elemento de uma lista
# OBS: O POP não somente remove o último elemento, como também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos a direita desse índice serão deslocados para a esquerda.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre eles.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# OBS: Abaixo estamos falando: Pega a lista6, coloca um espaço entre cada elemento e transforme em uma string
curso = ' '.join(lista6)
print(curso)

# OBS: Abaixo estamos falando: Pega a lista6, coloca um $ entre cada elemento e transforme em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 4126745817645]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

for elemento in lista2:
    print(elemento)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: \n')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa (funciona como um círculo)

print(cores[-1])  # branco
print(cores[-2])
print(cores[-3])
print(cores[-4])

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]

print(numeros.index(6))
print(numeros.index(9))

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5))

# Podemos fazer uma busca a partir de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # A partir do indice 1
print(numeros.index(5, 3))  # A partir do índice 3

# Podemos fazer uma busca dentro de um range, ou seja, início / fim
print(numeros.index(8,4, 8))  # Buscar o valor 8, entre os índices 3 a 6


# Revisão de slicing

# lista[inicio:fim:passo]
# lista(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1::])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])  # Começa em 0, pega até o índice 2 - 1
print(lista[:4])  # Começa em 0, pega até o índice 4 - 1
print(lista[1:3])  # Começa em 1, pega até o índice 3 - 1

# # Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(min(lista))  # minimo valor
print(max(lista))  # máximo valor
print(len(lista))  # tamanho da lista

# Transformar Lista em Tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

n1, n2, n3 = lista

print(n1)
print(n2)
print(n3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber dados, teremos um ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

nova.append(4)

print(lista)
print(nova)


# Veja que ao utilizarmos o lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python é
# chamado de Deep Copy

# Forma 2 - Shallow Copy


lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
# modificações em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
