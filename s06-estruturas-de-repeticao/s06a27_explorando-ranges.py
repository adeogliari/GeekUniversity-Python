"""
Ranges

    Precisamos conhecer o loop for para usar o range.
    Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada

Formas gerais:
    Forma 1
        range(valor_de_parada)
            //execução

        # OBS: valor_de_parada não inclusive (início padrão 0 e passo de 1 em 1)

        for num in range(5):
            print(num) //0, 1, 2, 3, 4

    Forma 2
        range(valor_de_inicio, valor_de_parada)

        # OBS: valor_de_parada não inclusive (início especificado pelo usuário e passo de 1 em 1)

        for num in range(1, 5):
            print(num) // 1, 2, 3, 4

    Forma 3
        range(valor_de_inicio, valor_de_parada, passo)

        # OBS: valor_de_parada não inclusive (valor_de_inicio e passo especificados pelo usuário)

        for num in range(1, 5, 2):
            print(num) // 1, 3,

    Forma 4 (inversa)
        range(valor_de_inicio, valor_de_parada, passo)

        # OBS: valor_de_parada não inclusive (valor_de_inicio e passo especificados pelo usuário)

        for num in range(5, 1, -1)
            print(num) // 4, 3, 2, 1
"""

