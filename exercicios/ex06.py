"""
Qual letra aparece mais vezes na frase?
"""

frase = input('Digite uma frase: ')
i = 0
maior = 0
letra_com_maior_incidencia = ''

while i < len(frase):
    letra = frase[i].lower()
    if letra == ' ':
        i += 1
        continue
    incidencias = frase.lower().count(letra)
    if incidencias > maior:
        maior = incidencias
        letra_com_maior_incidencia = letra
    i += 1
        
print(f'A letra com maior incidência na frase é "{letra_com_maior_incidencia}", aparecendo {maior} vezes')
        