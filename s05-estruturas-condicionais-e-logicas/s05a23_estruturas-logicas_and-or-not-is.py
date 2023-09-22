"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    not, is

Operadores binários:
    and, or
"""

ativo = True
logado = True
a, b, c, d = 2, 2, 3, 4

# not - Inverte o valor booleano
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# and - Compara e retorna True se tudo for True
elif ativo and logado:
    print('Bem-vindo usuário')

# is - Compara os valores e se forem iguais retorna True
if a is True:
    print('a = c')


# or - Compara os valores e se ao menos um for True retorna True
if b or d is c:
    print('b ou d = c')





