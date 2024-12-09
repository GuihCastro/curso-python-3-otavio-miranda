"""
Exercício 2: Função Decoradora com Argumentos
Crie uma função decoradora que adicione um prefixo e sufixo a um texto passado como argumento. A função decorada deve exibir um texto personalizado.

Requisitos:

A função decoradora deve receber dois parâmetros: prefixo e sufixo.
A função decorada deve ser chamada exibir_texto, e ela deve exibir o texto fornecido como argumento.

Exemplo de execução:
    @decorar_texto("Mensagem: ", " Fim da mensagem.")
    def exibir_texto(texto):
        print(texto)

    exibir_texto("Olá, isso é um teste!")
    
Saída esperada:
    Mensagem: Olá, isso é um teste! Fim da mensagem.
"""

def decorador_texto(txt_1, txt_2):
    def decoradora(func):
        def inner(msg):
            print(f'{txt_1} {msg} {txt_2}')
        return inner
    return decoradora


@decorador_texto('Mensagem', 'Fim da mensagem.')
def exibir_texto(texto):
    print(texto)
    
    
exibir_texto('Olá, isso é um teste!')
