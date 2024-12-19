"""
Context Manager com função (generator) 
    -> Criando e Usando gerenciadores de contexto (`contextlib.contextmanager`)
"""

from contextlib import contextmanager

@contextmanager
def my_open(path, mode, enc='utf-8'):
    try:
        print('Abrindo arquivo...')
        file = open(path, mode, encoding=enc)
        yield file
    except Exception as e:
        print('Deu pau: ', e)
    finally:
        print('Fechando arquivo...')
        file.close()


with my_open('.\\aulas\\aula120.txt', 'w') as file:
    print('Dentro do WITH...')
    file.write('Linha1\n')
    file.write('Linha2\n', 666)
    file.write('Linha3\n')
