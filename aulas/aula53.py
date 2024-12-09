"""
Shallow Copy vs Deep Copy
Cópias Rasas (shallow copy) não fazem a cópia de objetos mutáveis que existam no dicionário. Esses continuarão apontando para o mesmo objeto na memória.
Para se fazer uma cópia destes, é necessário realizar uma Cópia Profunda (deep copy), através do módulo copy.
"""

from copy import deepcopy

dicionario_1 = {
    'chave_1': 1,
    'chave_2': 2,
    'chave_3': [0, 1, 2],
}

dicionario_2 = dicionario_1.copy() # shallow copy
dicionario_3 = deepcopy(dicionario_2) # deep copy

dicionario_2['chave_3'][1] = 6 # afeta o original
dicionario_3['chave_3'][1] = 666 # não afeta o original

print(f'{dicionario_1=}\n{dicionario_2=}\n{dicionario_3=}')
