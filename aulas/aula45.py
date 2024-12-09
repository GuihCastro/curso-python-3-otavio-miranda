"""
Escopo de funções em Python
Escopo significa o local de onde aquele código pode ser atingido.
Existe o escopo global e local.
    -> O escopo global é o escopo onde todo o código é alcançavel de qualquer ponto.
    -> O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
    -> Escopos menores alcançam escopos maiores, mas escopos maiores não alcançam escopos menores.
    -> A palavra `global` faz uma variável do escopo interno ser a mesma do escopo externo.
"""


def escopo_local_1():
    global x
    x = 10
    
    def escopo_local_2():
        x = 11
        y = 2
        print(x, y)
        
    escopo_local_2()
    print(x)
    
    
x = 1

print(x)
escopo_local_1()
print(x)
