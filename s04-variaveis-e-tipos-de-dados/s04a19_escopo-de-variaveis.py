"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variáveis Locais;
    Variáveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco
    onde foi declarada

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela. Este tipo é inferido ao atribuírmos o valor à mesma.

    Exemplo em C:
        int numero = 42

    Exemplo em Java:
        int numero = 42

    PYTHON
        numero = 42
        print(numero)
        print(type(numero))

        numero = 'Geek'
        print(numero)
        print(type(numero))

        print(nao_existo)  # NameError devido à variável não estar definida

        numero = 2
        v_global = numero + 20

        if numero > 10:
            v_local = numero + 10
            print(v_local)

        print(v_global)
        print(v_local)
"""








