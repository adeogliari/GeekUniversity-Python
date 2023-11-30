"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula
"""

ativo = True
print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
    Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
    se for falso, o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)
logado = False

# Ou (or):
"""
    É uma operação binária, ou seja, depende de dois valores. É verdadeira quando ao menos 1 deles é verdadeiro.
    
    True or False -> True
    False or False -> False
"""

print(ativo or logado)

#E (and):
"""
É uma operação binária, ou seja, depende de dois valores. É verdadeira apenas quando ambos são verdadeiros.
    
    True or True -> True
    True or False -> False
"""


