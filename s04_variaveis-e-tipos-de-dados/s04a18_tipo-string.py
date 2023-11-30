"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
    # Estiver entre aspas simples -> 'uma string', '123', 'a', 'True', '42.3'
    # Estiver entre aspas duplas -> "uma string", "123", "a", "True", "42.3"
    # Estiver entre as simples triplas -> '''uma string''', '''123''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre as duplas triplas -> """uma string""", """123""", """a""", """True""", """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

nome = "Angelina \n Jolie"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

print(nome.lower())

print(nome.split())  # Transforma em uma lista de substrings com base em espaços em branco

print(nome[0:4])  # Slice de string

print(nome[::-1])  # inicio:fim:passos -> Do primeiro ao último elemento em ordem invertida

print(nome[::2])  # inicio:fim:passos -> Do primeiro ao último elemento a cada 2 elementos

print(nome.replace('e', 'i'))


