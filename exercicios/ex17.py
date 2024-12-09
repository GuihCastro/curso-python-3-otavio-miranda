"""
Sistema de perguntas e respostas
"""


def ler_resposta(msg):
    while True:
        resposta = input(msg).strip().lower()
        if len(resposta) == 1 and resposta.isalpha():
            return resposta
        print('Você deve inserir apenas uma letra correspondente à opção desejada. Tente novamente.')
        
        
def exibir_alternativas(opcoes):
    print('\nOPÇÕES:')
    for chave, valor in opcoes.items():
        print(f'{chave}) {valor}')



perguntas = [
    {
      'pergunta': 'Quanto é 2 + 2?',
      'opções': {
          'a': 1,
          'b': 3,
          'c': 4,
          'd': 5,
      },
      'resposta': 4,
    },
    {
      'pergunta': 'Quanto é 5 x 5?',
      'opções': {
          'a': 25,
          'b': 55,
          'c': 10,
          'd': 51,
      },
      'resposta': 25,
    },
    {
      'pergunta': 'Quanto é 10 ÷ 2?',
      'opções': {
          'a': 4,
          'b': 5,
          'c': 2,
          'd': 1,
      },
      'resposta': 5,
    },
]

acertos = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['pergunta']}')
    exibir_alternativas(pergunta['opções'])
    resposta_do_usuario = pergunta['opções'][ler_resposta('Escolha uma opção: ')]
    if resposta_do_usuario == pergunta['resposta']:
        print('Certa resposta! ✅')
        acertos += 1
    else:
        print('Resposta errada! ❌')
    print()
    
print(f'Fim de jogo!\nVocê acertou {acertos} de 3 perguntas.')
