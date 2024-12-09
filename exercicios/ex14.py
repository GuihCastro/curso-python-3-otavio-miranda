"""
Exercício com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
"""


def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


numbers = []

while True:
    try:
        arg = int(input('Informe um número para a operação: '))
        numbers.append(arg)
        break
    except ValueError:
        print('Por favor, informe apenas números.')
        
while True:
    try:
        arg = int(input('Informe pelo menos mais um: '))
        numbers.append(arg)
        break
    except ValueError:
        print('Por favor, informe apenas números.')
        
while True:
    more = input('Você deseja incluir mais números? (s/n): ').strip().lower()
    if more == 'n':
        break
    else:
        while True:
            try:
                arg = int(input('Informe o próximo número para a operação: '))
                numbers.append(arg)
                break
            except ValueError:
                print('Por favor, informe apenas números.')

result = multiply(*numbers)

print(f'O resultado dessa operação é: {result}')
