# método .format()

nome = 'Guilherme'
idade = 32
peso = 81
altura = 1.69
imc = peso / (altura * altura)

print('{n}, de {i} anos, tem {a:.2f} de altura e pesa {p} quilos'.format(n=nome, i=idade, a=altura, p=peso))
print('Seu IMC é: {:.1f}'.format(imc))
