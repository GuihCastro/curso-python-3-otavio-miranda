"""
Exercício - Lista de tarefas com desfazer e refazer

todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""


def add_item(item, list):
    list.append(item)
    print(f'"{item}" adicionada com sucesso à lista!\n')
    
    
def undo(main, backup):
    last_task = main.pop()
    backup.append(last_task)
    print(f'\n"{last_task}" removida com sucesso da lista!\n')
    
    
def redo(main, backup):
    recovered_task = backup.pop()
    main.append(recovered_task)
    print(f'\n"{recovered_task}" adicionada de volta à lista!\n')
    
    
def receive_integer_input(*args):
    # print(args)
    while True:
        try:
            integer = int(input('Informe o número da tarefa que deseja remover: '))
            if not check_index(args, integer-1):
                print('Não existe tarefa para o número informado.\n')
                continue
            break
        except ValueError:
            print('Informe apenas números.\n')
    return integer


def check_index(list, index):
    return 0 <= index < len(list)
    
    
def delete_task(list, index):
    deleted_task = list.pop(index)
    print(f'"{deleted_task}" foi deletada permanentemente!\n')
    
    
def show_list(list):
    for item in list:
        print(f'\t{item}')
    print()
    
    
def save_and_quit(list):
    with open(path, '+w', encoding='utf-8') as file:
        for item in list:
            file.write(f'{item}\n')
    print('A lista foi salva com sucesso!')
    

directory = '.\\exercicios\\arquivos\\'
path = directory+'todo_list.txt'

# todo_list = []
with open(path, '+a', encoding='utf-8') as file:
    file.seek(0, 0)
    todo_list = [line.strip() for line in file.readlines()]

backup_list = []

print(f'{todo_list=}')

while True:
    print('Escolha uma das opções a seguir:\n\t[1] Adicionar item\n\t[2] Desfazer\n\t[3] Refazer'
          '\n\t[4] Remover item (esta ação não pode ser desfeita)\n\t[5] Listar tarefas'
          '\n\t[0] Salvar e sair')
    option = input('Sua opção: ')

    match option:
        case '0':
            save_and_quit(todo_list)
            break
        case '1':
            task = input('\nTarefa a ser adicionada: ')
            if task not in todo_list:
                add_item(task, todo_list)
            else:
                print(f'"{task}" já está na lista.\n')
        case '2':
            if todo_list:
                undo(todo_list, backup_list)
            else:
                print('\nA lista de tarefas está vazia.\n')
        case '3':
            if backup_list:
                redo(todo_list, backup_list)
            else:
                print('\nNão há tarefas a serem recuperadas.\n')
        case '4':
            if todo_list:
                print('\nEscolha uma tarefa para remover:')
                for i, task in enumerate(todo_list):
                    print(f'\t{i+1} -> {task}')
                index_to_remove = receive_integer_input(*todo_list[:]) - 1
                delete_task(todo_list, index_to_remove)
            else:
                print('A lista de tarefas está vazia.\n')
        case '5':
            if todo_list:
                print('\nLista de tarefas:')
                show_list(todo_list)
            else:
                print('A lista de tarefas está vazia.\n')
