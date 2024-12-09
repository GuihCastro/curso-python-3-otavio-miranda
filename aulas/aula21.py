# Operadores Lógicos
# and (e), or (ou) e not (não / negação)
# São falsy: 0, 0.0 '' e False
# Existe também o None, que representa um não-valor

# Operador and

opcao = input('[E]ntrar ou [S]air: ')
senha = input('Informe a senha: ')
senha_valida = '123456'

if opcao == 'E' and senha == senha_valida:
    print('Entrando no sistema...')
else:
    print('Saindo do sistema...')
    
# NOTE! Checagens de curto circuito: Numa operação and, o Python para no primeiro valor False encontrado, e retorna o mesmo
 