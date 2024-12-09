"""
Gerador de CPFs aleatórios
Com base na versão completa do exercício anterior
"""

from random import randint

cpf = ''
for _ in range(9):
    cpf += str(randint(0, 9))

fator = 10
i = soma = 0

while fator >= 2:
    soma += int(cpf[i]) * fator
    i += 1
    fator -= 1
    
digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
    
cpf += str(digito_1)

fator = 11
i = soma = 0

while fator >= 2:
    soma += int(cpf[i]) * fator
    i += 1
    fator -= 1
    
digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
    
cpf += str(digito_2)

print(f'CPF gerado: {cpf}')
