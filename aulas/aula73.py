"""
Tratamento de esceções com try e except
A cláusula completa conta com: 
    try -> except -> else -> finally
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
except: 
    print('Erro desconhecido.')
    
print('Fim do programa.')
