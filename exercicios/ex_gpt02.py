"""
Exercício 2: Filtrar Palavras Curtas
Dada uma lista de palavras, utilize uma função lambda com filter para encontrar apenas as palavras com menos de 5 caracteres.

    Entrada: ["Python", "é", "muito", "legal", "de", "aprender"]
    Saída esperada: ["é", "de"]
"""

words = ["Python", "é", "muito", "legal", "de", "aprender"]
short_words = (list(filter(lambda word: len(word) < 5, words)))

print(f'{short_words=}')
