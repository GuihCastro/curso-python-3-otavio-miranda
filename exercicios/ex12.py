"""
Validar o cpf calculando os dois últimos digitos
(junção dos dois últimos exercícios)
"""

import re
import sys

cpf = re.sub(r'[^0-9]', '', input('Informe um CPF: '))

if cpf == len(cpf) * cpf[0]:
    print('Valores sequenciais não são válidos.')
    sys.exit()

cpf_calculado = cpf[:9]

fator = 10
i = soma = 0

while fator >= 2:
    soma += int(cpf_calculado[i]) * fator
    i += 1
    fator -= 1
    
digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
    
cpf_calculado += str(digito_1)

fator = 11
i = soma = 0

while fator >= 2:
    soma += int(cpf_calculado[i]) * fator
    i += 1
    fator -= 1
    
digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
    
cpf_calculado += str(digito_2)

print('CPF Válido!' if cpf_calculado == cpf else 'CPF Inválido!')
