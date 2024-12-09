"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
=================== resultado
    lista_soma  = [2, 4, 6, 8]
"""

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
    
lista_soma = [sum(nums) for nums in zip(lista_a, lista_b)]

print(f'{lista_soma=}')
