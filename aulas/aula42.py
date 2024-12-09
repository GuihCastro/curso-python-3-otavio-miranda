"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do código.
Elas podem receber valores como parâmetros (argumentos) e retornar ou não um valor específico.
Por padrão, funções retornam None (nada | não-valor).
"""

def greeting(name='User'):
    print(f'Hello, {name}!')
    
    
greeting('Gui')
greeting('Mari')
greeting()
