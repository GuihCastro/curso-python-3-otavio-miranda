"""
Iterando sobre strings
"""

nome = input('Nome: ')
tamanho = len(nome)
nova_string = ''
contador = 0

while contador < tamanho:
    nova_string += f'*{nome[contador].upper()}'
    contador += 1
    if contador == tamanho:
        nova_string += '*'
    
print(nova_string)
