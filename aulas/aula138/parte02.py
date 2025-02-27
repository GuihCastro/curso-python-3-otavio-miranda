"""argparse.ArgumentParser para argumentos mais complexos"""
# Tutorial Oficial: https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra o valor da opção -b ou --basic ("Hello, World!" por default)',
    type=str,  # tipo do argumento
    default=['Hello, World!'],  # valor padrão
    required=False,  # determina se o argumento é obrigatório
    nargs='+',  # recebe mais de um valor
    # action='append', # recebe o argumento mais de uma vez, mas não permite o uso de `type`, `default` e `nargs`
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra status de logs',
    action='store_true',  # não recebe valor, apenas ativa o argumento
)

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic.')
    print(args.basic)
else:
    print('Valor(es) de basic:')
    for indice, arg in enumerate(args.basic):
        if indice == len(args.basic) - 1:
            print(f'{indice}: {arg}\n')
        else:
            print(f'{indice}: {arg}', end=' | ')

print(f'Log status: {args.verbose}\n')
