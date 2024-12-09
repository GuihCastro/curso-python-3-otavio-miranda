"""
Exercício 4: Transformar Datas em Strings
Dada uma lista de datas no formato (ano, mês, dia), use uma função lambda com map para transformá-las em strings no formato "DD/MM/AAAA".

    Entrada: [(2024, 11, 28), (2023, 10, 15), (2025, 1, 9)]
    Saída esperada: ["28/11/2024", "15/10/2023", "09/01/2025"]
"""

dates = [(2024, 11, 28), (2023, 10, 15), (2025, 1, 9)]
formated_dates = list(map(lambda date: f'{date[2]:02}/{date[1]:02}/{date[0]}', dates))

print(f'{formated_dates=}')
