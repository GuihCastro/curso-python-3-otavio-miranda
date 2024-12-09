# Interpolação básica de strings
"""
usa-se %
s -> string
d e i -> int
f -> float
x e X -> Hexadecimal (ABCDEF0123456789)
"""

name = 'Guilherme'
price = 666.666

print('%s, o preço é R$%.2f' % (name, price))
print('O Hexadecimal de %d é %04X' % (666, 666))
