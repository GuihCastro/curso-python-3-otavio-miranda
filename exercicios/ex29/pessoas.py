"""Módulo de pessoas (Pessoa e Cliente)."""

from contas import Conta, TipoConta, ContaCorrente, ContaPoupanca


class Pessoa:
    """Classe de Pessoa."""

    def __init__(self, nome: str, idade: int) -> None:
        """Construtor da classe Pessoa.

        Args:
            nome (str): Nome da pessoa.
            idade (int): Idade da pessoa.
        """
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        """Getter do nome da pessoa."""
        return self._nome

    @property
    def idade(self) -> int:
        """Getter da idade da pessoa."""
        return self._idade


class Cliente(Pessoa):
    """Classe de Cliente."""

    def __init__(self, nome: str, idade: str) -> None:
        super().__init__(nome, idade)
        self._contas: list[Conta] = []

    @property
    def contas(self) -> list:
        """Getter da conta do cliente."""
        return self._contas

    def criar_conta(self, tipo: TipoConta, banco: object, agencia: int) -> Conta:
        """Método de criação de conta."""
        match tipo:
            case TipoConta.CORRENTE:
                conta = ContaCorrente(self, banco, agencia)
            case TipoConta.POUPANCA:
                conta = ContaPoupanca(self, banco, agencia)
            case _:
                raise ValueError('Tipo de conta inválido')
        self._contas.append(conta)
        print('-'*20)
        print(
            f'Conta {tipo.name} de número {conta.numero}, sob a titularidade de {self.nome} criada com sucesso!')
        print('-'*20)
        return conta

    def __repr__(self) -> str:
        """Representação da classe."""
        return f'Cliente({self.nome=}, {self.idade=})'
