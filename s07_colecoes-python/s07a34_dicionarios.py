"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave: valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))


# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(type(paises['eua']))

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))


"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

russia = paises.get('ru')

if russia:
    print(f'Encontrei o país {russia}')
else:
    print(f'Não encontrei o país {russia}')







