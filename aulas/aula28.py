# Exercício
"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu nome (não) contém espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {primeira_letra}
        A última letra do seu nome é {última_letra}
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou campos vazios."
"""

name = input('Digite o seu nome: ')
age = input('Digite a sua idade: ')

if not name or not age:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {name}.')
    print(f'Seu nome invertido é {name[::-1]}.')
    if ' ' in name:
        print('Seu nome CONTÉM espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
    print(f'Seu nome tem {len(name)} letras.')
    print(f'A primeira letra do seu nome é {name[0]}.')
    print(f'A última letra do seu nome é {name[-1]}.')
