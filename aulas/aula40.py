"""
split() e join() com list e str
split() -> Divide uma string, criando uma lista com cada um dos elementos (o padrão é palavra por palavras, mas podemos passar um elementro separador como argumento)
join() -> Une uma lista (passada como argumento) em uma string
"""

frase = 'Olha só que coisa mais interessante'
lista_de_palavras = frase.split()

print(frase)
print(lista_de_palavras)

nova_frase = '-'.join(lista_de_palavras)

print(nova_frase)
