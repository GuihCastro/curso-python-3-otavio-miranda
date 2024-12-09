"""
Operadores úteis para Sets
    -> union (união) -> `|` - une dois conjuntos, eliminando repetições;
    -> intersection (intersecção) -> `&` - pega os itens presentes em ambos;
    -> diferença -> `-` - pega os itens presentes apenas no set da esquerda;
    -> diferença simétrica - `^` - pega os itens que NÃO estão em ambos; 
"""

conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}

união = conjunto_1 | conjunto_2
intersecção = conjunto_1 & conjunto_2
diferença = conjunto_2 - conjunto_1
diferença_simétrica = conjunto_1 ^ conjunto_2

print(f'{conjunto_1=}\n{conjunto_2=}\n\n{união=}\n{intersecção=}\n{diferença=}\n{diferença_simétrica=}')
