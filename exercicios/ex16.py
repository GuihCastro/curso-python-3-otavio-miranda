"""
Exercício de Closure
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""


def make_multiplier(multiplier):
    def multiply(factor):
        return factor * multiplier
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

while True:
    try:
        number = int(input('Informe um número para realizar as operações: '))
        break
    except ValueError:
        print('Por favor, informe apenas números. Tente novamente.')

print(f'O dobro de {number} é: {double(number)}')
print(f'O triplo de {number} é: {triple(number)}')
print(f'O quadruplo de {number} é: {quadruple(number)}')
