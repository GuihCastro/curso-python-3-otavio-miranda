"""
Levantamento de exceções com `raise`
"""


def checar_tipagem(valor):
    if not valor.isnumeric():
        raise TypeError(f'Devem ser informados apenas valores numéricos, de tipo int ou float, e o valor "{valor}" informado é do tipo "{type(valor).__name__}"')
    return True
    
    
def checar_zero(div):
    if div == '0':
        raise ZeroDivisionError('O divisor não pode ser 0.')
    return True


def dividir(num, div):
    return float(num) / float(div)


x = input('Primeiro valor: ')
checar_tipagem(x)
y = input('Segundo valor: ')
checar_tipagem(y)
checar_zero(y)

print(f'A divisão de {x} por {y} dá: {dividir(x, y)}')
