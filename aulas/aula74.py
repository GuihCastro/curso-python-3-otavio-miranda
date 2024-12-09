"""
Parte 2 de tratamento de exceções
Capturando exceções não especificadas no except
"""

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    c = a / b
    # a[10]
except ValueError:
    print('Foi informado um valor não numérico.')
except ZeroDivisionError:
    print('Tentativa de divisão por 0.')
except Exception as error: 
    print(f'{error.__class__.__name__}: {error}')
    
print('Fim do programa.')
