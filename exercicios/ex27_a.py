"""
Exercício - Salve sua classe em JSON
    pt.1 -> Salve os dados da sua classe em JSON
"""

import json


class FamilyMember:
    family = 'Henrique de Castro Livraes'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_full_name(self):
        return f'{self.name} {__class__.family}'


def read_integer(msg):
    while True:
        try:
            value = int(input(msg))
            break
        except ValueError:
            print('Informe apenas números inteiros.')
    return value


def add_family_member():
    member = FamilyMember(
        input('Informe o nome: '),
        read_integer('Informe a idade: ')
    )
    # member = {
    #     'nome': input('Informe o nome: '),
    #     'age': read_integer('Informe a idade: ')
    # }
    family.append(member.__dict__)


def remove_last(list_to_remove, removed_list):
    if not list_to_remove:
        print('A lista já está vazia...')
        return
    removed_item = list_to_remove.pop()
    removed_list.append(removed_item)
    print(f'{removed_item} foi removido(a)!')
    
    
def recover_last(list_to_recover, removed_list):
    if not removed_list:
        print('Não há itens a serem recuperados...')
        return
    recovered = removed_list.pop()
    list_to_recover.append(recovered)
    print(f'{recovered} foi adicionado(a) de volta!')
    
    
def save_and_quit(obj):
    if not obj:
        print('A lista está vazia. Adicione algum item antes.')
        return
    with open(PATH, '+w', encoding='utf-8') as file:
        json.dump(obj, file, indent=2)
    print('Lista salva com sucesso!')
    
    
family = []
removed_members = []
PATH = '.\\exercicios\\arquivos\\ex27.json'
    

def register_system():
    while True:
        option = input(
            'Escolha uma opção:\n\t[1] Adicionar novo membro\n\t[2] Remover último\n\t[3] Recuperar último'
            '\n\t[0] Salvar e Sair\nSua opção: '
        )
        
        match option:
            case '0':
                save_and_quit(family)
                break
            case '1':
                add_family_member()
            case '2':
                remove_last(family, removed_members)
            case '3':
                recover_last(family, removed_members)
            case _:
                print('Informe uma opção válida.')
                
                
if __name__ == '__main__': register_system()
