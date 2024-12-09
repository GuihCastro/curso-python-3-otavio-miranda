"""
Solução mais simples para o exercício 23
"""

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']
estados_com_siglas = list(zip(estados, siglas)) # função built-in do Python

print(f'{estados_com_siglas=}')
