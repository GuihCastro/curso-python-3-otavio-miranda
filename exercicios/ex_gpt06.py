"""
Exercício 1: Função Decoradora Simples
Crie uma função decoradora que adicione uma mensagem antes e depois de chamar uma função. A função decorada deve simplesmente imprimir uma saudação.

Requisitos:

Crie uma função decoradora chamada mensagem_decorator que exiba uma mensagem antes e depois de qualquer função que ela decorar.
A função decorada deve ser chamada saudacao, e ela deve apenas imprimir "Olá, Mundo!".

Exemplo de execução:
    @mensagem_decorator
    def saudacao():
        print("Olá, Mundo!")

    saudacao()
    
Saída esperada:
    Antes da execução da função.
    Olá, Mundo!
    Depois da execução da função.
"""

def mensagem_decorator(func):
    def mensagem_decorada():
        print('Antes da execução da função.')
        func()
        print('Depois da execução da função.')
    return mensagem_decorada


@mensagem_decorator
def saudacao():
    print('Olá, Mundo!')
    
    
saudar = saudacao

saudar()
