"""
Argumentos nomeados e não nomeados (posicionais) em funções Python
|-> Argumento nomeado tem nome com sinal de igual
|-> Argumento não nomeado (posicional) recebe apenas o argumento (valor)
"""

def soma(x, y, z): # definição da função
    print(f'{x=}, {y=}, {z=} | x + y + z = {x+y+z}')
    
    
soma(1, 2, 3)
soma(1, y=2, z=5)
