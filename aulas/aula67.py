"""
Valores Truthy e Falsy em tipos Mutáveis e Imutáveis
    Mutáveis -> [], {} e set();
    Imutáveis -> (), '', 0, 0.0, None, False, range(0) 
"""

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nao_valor = None
booleano = False
intervalo = range(0)

falsy = lambda valor: 'Falsy' if not valor else 'Truthy'

print(f'TESTE -> {falsy('TESTE')}')
print(f'{lista=} -> {falsy(lista)}')
print(f'{dicionario=} -> {falsy(dicionario)}')
print(f'{conjunto=} -> {falsy(conjunto)}')
print(f'{tupla=} -> {falsy(tupla)}')
print(f'{string=} -> {falsy(string)}')
print(f'{inteiro=} -> {falsy(inteiro)}')
print(f'{flutuante=} -> {falsy(flutuante)}')
print(f'{nao_valor=} -> {falsy(nao_valor)}')
print(f'{booleano=} -> {falsy(booleano)}')
print(f'{intervalo=} -> {falsy(intervalo)}')
