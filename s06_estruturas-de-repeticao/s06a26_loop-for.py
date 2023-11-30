"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java
    for(int i = 0; i < 10; i++) {
        // execução do loop
    }

Python
    for item in iteravel:
        // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
    Exemplos de iteráveis
        String
            nome = 'Geek University'
        Lista
            lista = [1, 2, 3, 4, 5]
        Range
            numeros = range(1, 10)
"""

# Exemplo de for 1 (Iterando em uma string)
nome = 'Geek University'
for letra in nome:
    print(letra)

for letra in nome:
    print(letra, end='')  # Por default o print vem com end='\n' que faz com que cada print pule uma linha

# Exemplo de for 2 (Iterando sobre uma lista)
lista = [1, 3, 5, 7, 9]
for item in lista:
    print(item)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

"""
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome): 
    print(letra)
    
OBS: Quando não precisamos de um valor podemos descartá-lo utilizando o underline (_)
"""

for valor in enumerate(nome):
    print(valor[1], end='')


qtd = int(input('Quantas vezes esse loop deve rodar? \n'))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: \n'))
    soma += num

print(f'A soma é {soma}')


