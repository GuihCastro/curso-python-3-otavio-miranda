"""
Parte 3 de tratamento de exceções
Cláusulas else e finally
    else -> é executado quanto não ocorre um erro
    finally -> é executado de qualquer forma ao final do bloco
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
else:
    print('Tudo certo, nenhum erro.')
finally:
    print('Com ou sem erro, acabou esse trecho.\n')
    
print('Fim do programa.')
