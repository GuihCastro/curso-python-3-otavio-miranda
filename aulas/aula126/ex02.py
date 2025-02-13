"""Dataclass com `__post_init__`"""

from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = field(default=18)
    enderecos: list = field(default_factory=list)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


# Programa principal
if __name__ == '__main__':
    pessoa1 = Pessoa('Guilherme', 'Henrique de Castro', 32)
    print(pessoa1)
    print(f'{pessoa1.nome_completo=}')
