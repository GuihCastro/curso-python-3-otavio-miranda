"""
Funções Recursivas e Recursividade
Funções recursivas são funções que se chamam de volta (tem uma chamada a si mesma como seu retorno)
Funcionam de forma similar a loops, e são úteis para dividir problemas grandes em partes menores.
Toda função recursiva deve ter:
    -> Um problema maior que possa ser dividido em partes menores;
    -> Um caso recursivo que resolve o problema menor;
    -> Um caso base que para a recursão.
ex:
    -> Função recursiva para cálculo fatorial
"""


def recursiva(start=0, stop=10):
    if start >= stop:
        return stop
    start += 1
    return recursiva(start, stop)


def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n-1)


print(recursiva())
print(fatorial(5))
