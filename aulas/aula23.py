# Operador not

senha_informada = input('Digite a senha: ')
senha_correta = '123456'

if not (senha_informada == senha_correta):
    print('Senha incorreta.')
else:
    print('Senha correta.')
