"""
Exercício 3: Função Decoradora com Retorno
Crie uma função decoradora que modifique o valor retornado por uma função. A função decorada deve calcular a soma de dois números, e o decorador deve aumentar o valor retornado em 10%.

Requisitos:

Crie um decorador chamado aumentar_valor que modifica o valor retornado por uma função, aplicando um aumento de 10%.
A função decorada chamada soma deve somar dois números e retornar o valor.

Exemplo de execução:
    @aumentar_valor
    def soma(a, b):
        return a + b

    print(soma(10, 20))
    
Saída esperada:
    33.0  # 30 + 10% de aumento
"""

def aumentar_valor(func):
    def inner(a, b):
        soma = func(a, b)
        resultado = round(soma*1.1, 2)
        return resultado
    return inner


@aumentar_valor
def soma(a, b):
    return a + b


print(soma(10, 20))
