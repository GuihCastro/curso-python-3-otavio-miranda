# f strings

nome = 'Guilherme'
idade = 32
peso = 81
altura = 1.69
imc = peso / (altura * altura)

print(f'{nome}, de {idade} anos, tem {altura:.2f} de altura e pesa {peso} quilos')
print(f'Seu IMC é: {imc:.1f}')
