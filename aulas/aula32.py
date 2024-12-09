"""
Repetições
while (enquanto)
Executa uma ação (bloco de código) enquanto uma condição for verdadeira
Loop infinito -> quando a condição nunca se torna falsa e o loop não tem fim
"""

while True:
    nome = input('Qual o seu nome? ')
    
    if nome.lower() == 'sair':
        break
    
    print(f'Seu nome é {nome}')
    
print('Saí do loop')
