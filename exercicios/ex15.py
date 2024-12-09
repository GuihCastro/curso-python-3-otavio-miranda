"""
Exercício com funções

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
"""


def even_odd(num):
    return 'PAR' if num % 2 == 0 else 'ÍMPAR'


while True:
    try:
        number = int(input('Informe um número para checar se é par ou ímpar: '))
        break
    except ValueError:
        print('Por favor, informe apenas números.')
        
print(f'O número {number} é {even_odd(number)}.')
