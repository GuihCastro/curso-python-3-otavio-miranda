# Flag, is, is not e None
"""
Flag (Bandeira) -> marca um ponto do código
None -> Não-valor
`is` e `is not` -> é ou não é (muito similar a `==` e `!=`)
id (Identidade) -> endereço de algo (variável, função, etc) na memória
"""

condition = True
flag = None

print(f'{flag=}')

if condition:
    flag = True
    print('Faça algo.')
else:
    print('Não faça algo.')
    
print(f'{flag=}')

if flag is None:
    print('Não passou no if.')
elif flag is not None:
    print('Passou no if.')
