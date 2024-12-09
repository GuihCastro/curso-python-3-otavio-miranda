# Formatação básica de strings
"""
com f-strings:
s -> string
d -> int
.<número-de-dígitos>f
x ou X -> Hexadecimal
(Caractere)(><^)(quantidade)
> -> posicionar à esquerda
< -> à direita
^ -> ao centro
sinal -> + ou -
Ex.: 0>-100,.1f
Conversion Flags -> !r !s !a
"""

value = 'ABC'
print(f'{value}.')
print(f'{value:>10}.')
print(f'{value:<10}.')
print(f'{value:^10}.')
print(f'{1000.666:0=+10,.1f}')
print(f'O Hexadecimal de 666 é {666:04X}')
print(f'{value!r}')
