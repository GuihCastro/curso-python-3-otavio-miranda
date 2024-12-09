"""
Cálculo do segundo digito para validação do CPF
CPf: 623.967.060-04
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO CALCULADO ANTERIORMENTE, multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.: 623.967.060-04 (6239670600)
    11 10  9  8  7  6  5  4  3  2
*    6  2  3  9  6  7  0  6  0  0
    66 20 27 72 42 42  0 24  0  0
    
Somar todos os resultados:
66+20+27+72+42+42+0+24+0+0 = 293
Multiplicar o resultado anterior por 10
293 * 10 = 2930
Obter o resto da divisão da conta anterior por 11
2930 % 11 = 4
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta
    
O primeiro digito desse CPF é 0
"""

cpf = '623.967.060-04'
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf_1 = cpf[:9] + '0'

fator = 11
i = soma = 0

while fator >= 2:
    soma += int(cpf_1[i]) * fator
    i += 1
    fator -= 1
    
digito = (soma * 10) % 11
digito = digito if digito <= 9 else 0
    
print(digito)
