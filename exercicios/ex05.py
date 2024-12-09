"""
Calculadora com while
"""

while True:
    while True:
        try:
            n1 = int(input('Primeiro número: '))
            break
        except:
            print('Por favor, informe um numeral válido.')
            
    while True:
        try:
            n2 = int(input('Segundo número: '))
            break
        except:
            print('Por favor, informe um numeral válido.')
            
    operacao = input('Operação de desejada (+, -, * ou /): ')
    while operacao not in '+-*/' or len(operacao) > 1:
        operacao = input('Opção inválida, tente novamente. (+, -, * ou /): ')
        
    resultado = 0        
    match operacao:
        case '+': resultado = n1 + n2
        case '-': resultado = n1 - n2
        case '*': resultado = n1 * n2
        case '/': resultado = n1 / n2
        
    print(f'{n1} {operacao} {n2} = {resultado}')
    
    continuar = input('Deseja continuar? [s]im: ').lower().startswith('s')
    if not continuar:
        break
    
print('Até logo!')
