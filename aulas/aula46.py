"""
Retorno de valores das funções (return)
"""


def subtracao(x, y):
    if x < y:
        return 'Não dá pra subtrair'
    return x - y


sub1 = subtracao(6, 3)
sub2 = subtracao(9, 3)
sub3 = subtracao(3, 6)

print(sub1)
print(sub2)
print(sub3)
