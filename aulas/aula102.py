"""
`@property` + `@property.setter` - getter e setter no modo Pythônico
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Atributos que começam com um ou dois underscores não devem ser usados fora da classe.
 🐍🤓🤯🤯🤯🤯
"""


class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        print('Mudando de cor...')
        self._cor = nova_cor


caneta = Caneta('Azul')

print(f'Cor da caneta: {caneta.cor}')

caneta.cor = 'Preta'

print(f'Cor da caneta: {caneta.cor}')

caneta.cor = 'Vermelha'

print(f'Cor da caneta: {caneta.cor}')
