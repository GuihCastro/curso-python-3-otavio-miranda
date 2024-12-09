# Operadores in e not in
# Checam se uma coisa está (ou não) contida em outra

name = input('Digite um nome: ')

if 'a' in name.lower():
    print(f'O nome "{name}" tem a letra "a".')
else:
    print(f'O nome "{name}" não tem a letra "a".')
