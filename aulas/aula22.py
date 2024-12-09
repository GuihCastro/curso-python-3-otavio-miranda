# Operador or

opcao = input('[E]ntrar ou [S]air: ')
senha = input('Informe a senha: ') or 'Sem senha'
print(f'{senha=}')
senha_valida = '123456'

if (opcao == 'E' or opcao == 'e') and senha == senha_valida:
    print('Entrando no sistema...')
else:
    print('Saindo do sistema...')
    
# NOTE! Checagens de curto circuito: Numa operação or, o Python para no primeiro valor True encontrado, e retorna o mesmo
