"""
Cálculo do primeiro digito para validação do CPF
CPf: 623.967.060-04
Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.: 623.967.060-04 (623967060)
    10  9  8  7  6  5  4  3  2
*    6  2  3  9  6  7  0  6  0
    60 18 24 63 36 35  0 18  0
    
Somar todos os resultados:
60+18+24+63+36+35+0+18+0 = 254
Multiplicar o resultado anterior por 10
254 * 10 = 2540
Obter o resto da divisão da conta anterior por 11
2540 % 11 = 10
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta
    
O primeiro digito desse CPF é 0
"""

cpf = '623.967.060-04'
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

fator = 10
i = soma = 0

while fator >= 2:
    soma += int(cpf[i]) * fator
    i += 1
    fator -= 1
    
digito = (soma * 10) % 11
digito = digito if digito <= 9 else 0
    
print(digito)
