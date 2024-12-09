# condicionais: if / elif / else

opcao = input('Você deseja entrar ou sair? ')

if opcao.lower() == 'entrar':
    print('Você entrou no sistema.')
elif opcao.lower() == 'sair':
    print('Você saiu do sistema.')
else:
    print('Você não optou por entrar nem sair do sistema.')
