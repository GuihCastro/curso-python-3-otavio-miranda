# fluxo do interpretador em condicionais

condicao_1 = True
condicao_2 = False
condicao_3 = True
condicao_4 = False

if condicao_1:
    print('Condição 1 satisfeita.')
    
if condicao_2:
    print('Condicao 2 satisfeita.')

if condicao_3:
    print('Condição 3 satisfeita.')
    
if condicao_4:
    print('Condição 4 satisfeita.')

if condicao_1 and condicao_2 and condicao_3 and condicao_4:
    print('Todas as condições satisfeitas.')
elif not condicao_1 and not condicao_2 and not condicao_3 and not condicao_4:
    print('Nenhuma condição satisfeita.')
else: 
    print('Somente algumas condições satisfeitas.')
