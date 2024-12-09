"""
`groupby()` -> Agrupando valores (`itertools`)
"""

from itertools import groupby


def ordenar_por_nota(aluno):
    return aluno['nota']


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos_por_nota = sorted(alunos, key=ordenar_por_nota)

alunos_por_nota = [
    (nota, list(grupo))
    for nota, grupo in groupby(
        sorted(alunos, key=ordenar_por_nota), 
        key=ordenar_por_nota
    )
]

for grupo in alunos_por_nota:
    print(f'Alunos que tiraram {grupo[0]}:')
    for aluno in grupo[1]:
        if grupo[1].index(aluno) < len(grupo[1])-1:
            print(aluno['nome'], end=', ')
        else:
            print(aluno['nome'])
    print()      
