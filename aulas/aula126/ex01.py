"""Dataclasses

O que são dataclasses?
    > O módulo dataclasses fornece um decorador e funções para criar métodos como _init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuário.

Em resumo: dataclasses são syntax sugar para criar classes normais.
Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.

    * doc: https://docs.python.org/3/library/dataclasses.html
"""

from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = field(default=18)
    enderecos: list[str] = field(default_factory=list)

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split(' ')
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


# Programa principal
if __name__ == '__main__':
    pessoa1 = Pessoa('Guilherme', 'Henrique de Castro')
    print(pessoa1)
    print(f'{pessoa1.nome_completo}')
