"""
Métodos de listas
    append() -> Adiciona um item ao final da lista;
    insert() -> Adiciona um item no índice passado como argumento;
    pop() -> Remove (e retorna) um item do final da lista (ou do índice passado como argumento);
    del -> Deleta um elemento da lista;
    clear() -> Limpa a lista;
    extend() -> Concatena uma lista (passada como argumento) em outra (que chama o método);
CRUD -> Create, Read, Update e Delete
"""

lista = [10, 20, 30, 40]

print(lista)

lista.append(50)
lista.append(60)
lista.append(70)

print(lista)

removido = lista.pop()

print(f'{lista}\nRemovido: {removido}')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

print(f'{lista_a = }')

lista_a.extend(lista_b)

print(f'{lista_a = }')
