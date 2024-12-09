from aula79_package.modulo_b import falar_oi

__all__ = [
    'soma',
    'variavel',    
]


def soma(*args):
    return sum(args)


variavel = 'Variável'
outra_variavel = 'Outra variável' # ficou de fora do `import *`