"""
Exercício 5: Agrupar Valores por Paridade
Você tem uma lista de números inteiros e precisa criar duas listas: uma com os números pares e outra com os números ímpares, utilizando duas funções lambda com filter.

    Entrada: [10, 15, 20, 25, 30, 35]
    Saída esperada:
        pares = [10, 20, 30]
        ímpares = [15, 25, 35]
""" 

integers = [10, 15, 20, 25, 30, 35]
even = list(filter(lambda num: num % 2 == 0, integers))
odd = list(filter(lambda num: num % 2 != 0, integers))

print(f'{even=}\n{odd=}')
