# Fatiamento de strings e função len()
"""
 Hello World
 012345678910
-10987654321
Fatiamento -> [início:fim:passo] | [::]
A função `len()` retorna a quantidade de caractéres da string passada como argumento
"""

txt: str = 'Hello World'
print(txt[2:7])
print(txt[::-1]) # de trás para frente
print(len(txt))
