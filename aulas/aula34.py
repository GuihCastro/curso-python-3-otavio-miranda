"""
continue
Interrompe a execução daquela iteração do loop
"""

contador = 0

while True:
    contador += 1
    
    if 10 <= contador <= 15:
        continue
    
    print(contador)
    
    if contador == 40:
        break
    
print('Saí do loop')
