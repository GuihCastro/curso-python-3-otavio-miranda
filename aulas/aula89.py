"""
Criando arquivos com Python + Context Manager with
Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)

Modos:
    -> `r`: leitura
    -> `w`: escrita
    -> `x`: para criação
    -> `a`: escreve ao final
    -> `b`: binário
    -> `t`: modo texto
    -> `+`: leitura e escrita
    
Context manager :
    -> `with`: abre e fecha o arquivo

Métodos úteis:
    -> `write` e `read`: escrever e ler
    -> `writelines`: escrever várias linhas
    -> `seek`: move o cursor
    -> `readline`: ler linha
    -> `readlines`: ler linhas
    
Básico sobre o módulo `os`:
    -> `os.remove` ou `os.unlink`: apaga o arquivo
    -> `os.rename`: troca o nome ou move o arquivo
    
Básico sobre o módulo `json`:
    -> `json.dump`: Gera um arquivo json
    -> `json.load`
"""

caminho = '.\\aulas\\arquivos\\'
caminho += 'aula89.txt'

# arquivo = open(caminho, 'w')
# arquivo.close()

# with open(caminho, 'w') as arquivo:  # utilizando o context manager
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    
# with open(caminho, 'r') as arquivo:
#     print(arquivo.read())
    
with open(caminho, 'w+') as arquivo:
    print('Escrevendo...')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    
    print('Movendo cursor para o início...')
    arquivo.seek(0, 0)
    
    print('Lendo primeira linha...')
    print(arquivo.readline(), end='')
    
    print('Lendo segunda linha...')
    print(arquivo.readline(), end='')
    
    print('Lendo demais linhas...')
    for linha in arquivo.readlines():
        print(linha, end='')
