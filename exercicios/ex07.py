"""
Jogo da Forca
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    -> Se a letra digitada estiver na palavra secreta: exiba a letra;
    -> Se a letra digitada não estiver na palavra secreta: exiba *;
- Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = 'Python'
palavra_escondida = len(palavra_secreta) * '*'
tentativas = 0

while True:
    tentativas += 1
    print(f'Adivinhe a palavra: {palavra_escondida}')
    letra = input('Chute uma letra (apenas uma): ')
    while len(letra) > 1:
        letra = input('Informe apenas uma letra. Tente novamente: ')
    if letra.lower() in palavra_secreta.lower():
        print(f'Correto! A palavra secreta tem a letra "{letra}"')
        nova_palavra_escondida = ''
        for i in range(len(palavra_secreta)):
            if palavra_escondida[i] == '*':
                if palavra_secreta[i].lower() == letra.lower():
                    nova_palavra_escondida += palavra_secreta[i]
                else:
                    nova_palavra_escondida += '*'
            else:
                nova_palavra_escondida += palavra_escondida[i]
        palavra_escondida = nova_palavra_escondida
    else:
        print(f'Errado! A palavra secreta não tem a letra "{letra}". Tente novamente')
    if '*' not in palavra_escondida:
        os.system('clear')
        print(f'A palavra secreta era: {palavra_secreta}\nPARABÉNS! Você acertou com {tentativas} tentativas.')
        continuar = input('Você deseja continuar? [s]im ou [n]ão: ').lower()
        if continuar == 's':
            os.system('clear')
            print('Ok! Vamos lá...')
            palavra_secreta = 'Java'
            palavra_escondida = len(palavra_secreta) * '*'
            tentativas = 0
        else:
            print('Obrigado por jogar!')
            break
                