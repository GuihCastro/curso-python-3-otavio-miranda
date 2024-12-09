"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista_de_compras = []

while True:
    opcao = int(input('Informe a opção desejada ([1] listar | [2] inserir | [3] excluir | [0] sair): '))
    while opcao < 0 or opcao > 3:
        opcao = int(input('Informe uma opção válida ([1] listar | [2] inserir | [3] excluir | [0] sair): '))
    match opcao:
        case 1:
            if not lista_de_compras:
                print('Sua lista está vazia. Insira algum item.')
            else:
                print('LISTA DE COMPRAS:')
                for item in lista_de_compras:
                    print(item)
        case 2:
            novo_item = input('Digite o item que deseja inserir na lista: ')
            lista_de_compras.append(novo_item)
            print(f'{novo_item} inserido com sucesso! Sua lista foi atualizada.')
        case 3:
            print('Escolha o item que deseja excluir a partir do índice')
            for i, item in enumerate(lista_de_compras):
                print(i, item)
            try:
                indice_para_excluir = int(input('Informe o índice desejado: '))
                item_excluido = lista_de_compras.pop(indice_para_excluir)
                print(f'{item_excluido} removido com sucesso! Sua lista foi atualizada.')
            except ValueError:
                print('Por favor, utilize apenas números.')
            except IndexError:
                print('O índice informado não existe na lista.')
        case 0:
            break
        
print('Obrigado por usar Sua Lista de Compras!')
