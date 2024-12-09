# Introdução ao try/except
"""
try -> tenta executar um bloco de código
except -> executa uma ação caso haja um erro no bloco do try
"""

valor_digitado: str = input('Vou dobrar o número que você digitar: ')

try:
    numero: float = float(valor_digitado)
    print(f'O dobro de {numero} é {numero * 2:.1f}')
except:
    print('O valor digitado não é um número.')
