# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def operacao(y):
        return funcao(x, y)
    return operacao


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

y = int(input('Informe um número para somar com 5 e multiplicar por 10: '))

print(f'{y} + 5 = {soma_com_cinco(y)}\n{y} x 10 = {multiplica_por_dez(y)}')
