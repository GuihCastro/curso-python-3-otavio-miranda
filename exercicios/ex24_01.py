"""
Solução alternativa do exercício 24 utilizando o zip_longest
"""

from itertools import zip_longest

lista_a = []
while True:
    while True:
        try:
            num = float(input('Informe um valor para ser adicionado na lista a ("0" para parar): '))
            break
        except ValueError:
            print('Por favor, informe apenas valores numéricos. Tente novamente.')
    if num == 0:
        break
    lista_a.append(num)
    
print()
    
lista_b = []
while True:
    while True:
        try:
            num = float(input('Informe um valor para ser adicionado na lista b ("0" para parar): '))
            break
        except ValueError:
            print('Por favor, informe apenas valores numéricos. Tente novamente.')
    if num == 0:
        break
    lista_b.append(num)
    
print()
    
lista_soma = [sum(nums) for nums in zip_longest(lista_a, lista_b, fillvalue=0)]

print(f'{lista_soma=}')
