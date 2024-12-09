"""
Exercício 5: Decorador com Função Aninhada e Parâmetros Variáveis
Crie um decorador que aceite parâmetros variáveis e use uma função aninhada dentro dele. O decorador deve calcular a média de vários números passados para a função decorada, mas a cada chamada, o decorador deve imprimir a quantidade de números processados.

Requisitos:

Crie o decorador decorar_media que aceita parâmetros variáveis e dentro dele, utilize uma função aninhada para calcular a média.
A função decorada chamada calcular_media deve receber uma lista de números e calcular a média.
O decorador deve exibir quantos números estão sendo processados antes de calcular a média.

Exemplo de execução:
    @decorar_media
    def calcular_media(*numeros):
        return sum(numeros) / len(numeros)

    print(calcular_media(10, 20, 30, 40))
    
Saída esperada:
    Calculando a média de 4 números.
    A média é: 25.0
"""

def decorar_media(func):
    def inner(*args):
        # print(f'Calculando a média de {len(args)} números.')
        return f'Calculando a média de {len(args)} números.\nA média é: {func(*args)}'
    return inner


@decorar_media
def calcular_media(*numeros):
    return sum(numeros) / len(numeros)


print(calcular_media(10, 20, 30, 40))
