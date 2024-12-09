"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

while True:
    try:
        horario = int(input('Informe o horário: '))
        if 0 <= horario < 12:
            print('Bom dia!')
            break
        elif 12 <= horario < 18:
            print('Boa tarde!')
            break
        elif 18 <= horario < 24:
            print('Boa noite!')
            break
        else:
            print('Não conheço esse horário.')
    except (TypeError, ValueError):
        print('Digite apenas números inteiros. Tente novamente')
