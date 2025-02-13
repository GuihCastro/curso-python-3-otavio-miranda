"""Módulo de contas (Conta, ContaCorrente e ContaPoupanca)."""

from abc import ABC, abstractmethod
from enum import Enum, auto
# from pessoas import Cliente


class TipoConta(Enum):
    """Enum de tipos de conta."""
    CORRENTE = auto()
    POUPANCA = auto()


class Conta(ABC):
    """Classe abstrata de Conta."""
    contador = 0

    def __init__(self, titular: object, banco: object, agencia: int) -> None:
        """Construtor da classe Conta.

        Args:
            agencia (int): Agência da conta.
        """
        self._titular = titular
        self._banco = banco
        self._agencia = agencia
        Conta.contador += 1
        self._numero: int = Conta.contador
        self.__saldo: float = 0.0

    @property
    def titular(self) -> object:
        """Getter do titular da conta."""
        return self._titular

    @property
    def banco(self) -> object:
        """Getter do banco da conta."""
        return self._banco

    @property
    def agencia(self) -> int:
        """Getter da agência da conta."""
        return self._agencia

    @property
    def numero(self) -> int:
        """Getter do número da conta."""
        return self._numero

    @property
    def saldo(self) -> float:
        """Getter do saldo da conta."""
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo: float) -> None:
        """Setter do saldo da conta."""
        self.__saldo = novo_saldo

    @abstractmethod
    def sacar(self, valor: float) -> None:
        """Método abstrato de saque."""
        pass

    def depositar(self, valor: float) -> None:
        """Método de depósito."""
        self.saldo += valor
        print('-'*20)
        print(
            f'Depósito de R${valor:.2f} realizado com sucesso na conta {self.numero} de {self.titular.nome}!')
        print(f'Saldo atual: R${self.saldo:.2f}')
        print('-'*20)

    def __repr__(self) -> str:
        """Representação da classe."""
        return f'Conta(agência={self.agencia}, número={self.numero}, saldo={self.saldo})'


class ContaCorrente(Conta):
    """Classe concreta de Conta Corrente."""

    def __init__(self, titular: object, banco: object, agencia: int) -> None:
        """Construtor da classe Conta Corrente.

        Args:
            agencia (int): Agência da conta.
        """
        super().__init__(titular, banco, agencia)
        self._cheque_especial: float = 500.0

    @property
    def cheque_especial(self) -> float:
        """Getter do cheque especial."""
        return self._cheque_especial

    @cheque_especial.setter
    def cheque_especial(self, novo_cheque_especial: float) -> None:
        """Setter do cheque especial."""
        self._cheque_especial = novo_cheque_especial

    def sacar(self, valor: float) -> None:
        """Método de saque.

        Args:
            valor (float): Valor do saque.

        Raises:
            ValueError: Se a autenticação do banco falhar ou o saldo for insuficiente.
        """
        if not self.banco.autenticar(self.titular, self):
            raise ValueError('Falha de autenticação do banco')
        if valor > self.saldo + self.cheque_especial:
            raise ValueError(
                f'Saldo insuficiente na conta {self.numero} de {self.titular.nome}!')
        if valor > self.saldo:
            self.cheque_especial -= valor - self.saldo
            self.saldo = 0
            print('-'*20)
            print(
                f'Saque de R${valor:.2f} realizado com sucesso na conta {self.numero} de {self.titular.nome}!')
            print(f'Saldo atual: R${self.saldo:.2f}')
            print(f'Cheque especial atual: R${self.cheque_especial:.2f}')
            print('-'*20)
        else:
            self.saldo -= valor
            print('-'*20)
            print(
                f'Saque de R${valor:.2f} realizado com sucesso na conta {self.numero} de {self.titular.nome}!')
            print(f'Saldo atual: R${self.saldo:.2f}')
            print(f'Cheque especial atual: R${self.cheque_especial:.2f}')
            print('-'*20)


class ContaPoupanca(Conta):
    """Classe concreta de Conta Poupança."""

    def __init__(self, titular: object, banco: object, agencia: int) -> None:
        """Construtor da classe Conta Poupança.

        Args:
            agencia (int): Agência da conta.
        """
        super().__init__(titular, banco, agencia)

    def sacar(self, valor: float) -> None:
        """Método de saque da Conta Poupança.

        Args:
            valor (float): Valor do saque.

        Raises:
            ValueError: Se a autenticação do banco falhar ou o valor do saque for maior que o saldo da conta.
        """
        if not self.banco.autenticar(self.titular, self):
            raise ValueError('Falha de autenticação do banco')
        if valor > self.saldo:
            raise ValueError(
                f'Saldo insuficiente na conta {self.numero} de {self.titular.nome}!')
        self.saldo -= valor
        print('-'*20)
        print(
            f'Saque de R${valor:.2f} realizado com sucesso na conta {self.numero} de {self.titular.nome}!')
        print(f'Saldo atual: R${self.saldo:.2f}')
        print('-'*20)
