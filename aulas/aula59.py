"""
Exemplificação de funções lambdas complexas
"""


def executar(func, *args):
    return func(*args)


def somar(x, y):
    return x + y


def somar_varios(*args):
    return sum(args)


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar


# print(somar(3, 3))
print(executar(lambda x, y: x + y, 3, 3))

# print(somar_varios(1, 2, 3, 4, 5, 6))
print(executar(lambda *args: sum(args), 1, 2, 3, 4, 5, 6))

# duplicar = criar_multiplicador(2)
duplicar = executar(lambda m: lambda n: m * n, 2)

print(duplicar(6))
