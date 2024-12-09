"""
Exercício 4: Decoradores com Função de Contagem de Execuções
Crie uma função decoradora que conte o número de vezes que uma função é chamada. A função decorada deve exibir uma mensagem toda vez que for executada.

Requisitos:

Crie um decorador chamado contador_execucoes que conta quantas vezes a função decorada foi chamada.
A função decorada chamada dizer_oi deve apenas imprimir "Oi!".
Exiba o número de vezes que a função foi chamada.

Exemplo de execução:
    @contador_execucoes
    def dizer_oi():
        print("Oi!")

    dizer_oi()
    dizer_oi()
    dizer_oi()

Saída esperada:
    Oi!
    Função chamada 1 vez.
    Oi!
    Função chamada 2 vezes.
    Oi!
    Função chamada 3 vezes.
"""

def contador_execucoes(func):
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        func()
        print(f'Função chamada {counter} vez(es).')    
    return inner


@contador_execucoes
def dizer_oi():
    print('Oi!')
    
    
dizer_oi()
dizer_oi()
dizer_oi()
