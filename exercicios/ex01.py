"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

while True:
    try:
        number = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('O que você digitou não é um número inteiro. Tente novamente.')
        
if number % 2 == 0:
    print(f'{number} é PAR')
else:
    print(f'{number} é ÍMPAR')
