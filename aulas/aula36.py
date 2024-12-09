"""
Laço de repetição for
Utilizamos em casos em que temos controle sobre o número de repetições
"""

nome = input('Digite um nome: ')
novo_nome = ''

for letra in nome:
    novo_nome += f'*{letra}'
    
novo_nome += '*'

print(novo_nome)
