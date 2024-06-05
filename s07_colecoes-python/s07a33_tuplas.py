"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:
    1 - As tuplas são representadas por parênteses ()

    2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma Tupla gera
    uma nova Tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:
    tupla1 = (1, 2, 3, 4, 5, 6)
    tupla2 = 1, 2, 3, 4, 5, 6

# CUIDADO 2: Tuplas com 1 elemento
    tupla3 = (3) # Isso não é uma tupla

    tupla4 = (4,) # Isso é uma tupla
    tupla5 = 5, # Isso é uma tupla

# CONCLUSÃO: Podemos concluir que as tuplas são definidas pela vírgula e não pelo uso do parênteses

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(10))


# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho; * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(min(tupla))
print(max(tupla))
print(sum(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)


# Tuplas são imutáveis, mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla2
print(tupla1)


# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)

print(3 in tupla)


# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas
    1 - Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção


"""

# Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista