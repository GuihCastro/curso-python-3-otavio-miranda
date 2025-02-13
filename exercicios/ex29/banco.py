"""Módulo de banco."""

from pessoas import Cliente
from contas import Conta, TipoConta


class Banco:
    """Classe concreta de Banco."""

    def __init__(self, nome: str) -> None:
        """Construtor da classe Banco.

        Args:
            nome (str): Nome do banco.
        Attributes:
            nome (str): Nome do banco.
            clientes (list[Cliente]): Lista de clientes do banco.
            contas (list[Conta]): Lista de contas do banco.
            agencias (list[int]): Lista de agências do banco.
            numero_agencias (int): Número de agências do banco.
            numero_contas (int): Número de contas do banco.
            numero_clientes (int): Número de clientes do banco.
        """
        self._nome: str = nome
        self._clientes: list[Cliente] = []
        self._contas: list[Conta] = []
        self._agencias: list[int] = [1111, 2222, 3333]
        self._numero_agencias: int = len(self._agencias)
        self._numero_contas: int = len(self._contas)
        self._numero_clientes: int = len(self._clientes)

    @property
    def nome(self) -> str:
        """Getter do nome do banco.

        Returns:
            str: Nome do banco.
        """
        return self._nome

    @property
    def clientes(self) -> list[Cliente]:
        """Getter da lista de clientes do banco.

        Returns:
            list[Cliente]: Lista de clientes do banco.
        """
        return self._clientes

    @property
    def contas(self) -> list[Conta]:
        """Getter da lista de contas do banco.

        Returns:
            list[Conta]: Lista de contas do banco.
        """
        return self._contas

    @property
    def agencias(self) -> list[int]:
        """Getter da lista de agências do banco."""
        return self._agencias

    def cadastrar_cliente(self, nome: str, idade: int) -> Cliente:
        """Método de cadastro de Clientes.

        Args:
            nome (str): Nome do cliente.
            idade (int): Idade do cliente.
        """
        cliente = Cliente(nome, idade)
        self._clientes.append(cliente)
        print(f'Cliente {cliente.nome} cadastrado com sucesso!')
        return cliente

    def adicionar_conta(self, cliente: Cliente, tipo: TipoConta, agencia: int) -> None:
        """Método de adição de contas.

        Args:
            cliente (Cliente): Cliente da conta.
            tipo (TipoConta): Tipo da conta.
            agencia (int): Agência da conta.
        Raises:
            ValueError: Se a agência não existir.
        """
        if agencia not in self._agencias:
            raise ValueError('Agência inválida')
        conta = cliente.criar_conta(tipo, self, agencia)
        self._contas.append(conta)

    def autenticar(self, cliente: Cliente, conta: Conta) -> bool:
        """Método de autenticação.

        Returns:
            bool: True se o cliente e a conta forem válidos, False caso contrário.
        """
        autenticado = self._checar_cliente(cliente) and self._checar_conta(
            conta, cliente) and self._checar_agencia(conta.agencia)
        if not autenticado:
            print('Falha na autenticação')
        return autenticado

    def _checar_cliente(self, cliente: Cliente) -> bool:
        """Método de checagem de cliente."""
        if cliente not in self.clientes:
            raise ValueError('Cliente não cadastrado neste banco.')
        return True

    def _checar_conta(self, conta: Conta, cliente: Cliente) -> bool:
        """Método de checagem de conta."""
        if conta not in self.contas:
            raise ValueError('Conta não cadastrada neste banco.')
        if conta.titular != cliente:
            raise ValueError('Conta não pertence ao cliente.')
        return True

    def _checar_agencia(self, agencia: Conta.agencia) -> bool:
        """Método de checagem de agência."""
        if agencia not in self.agencias:
            raise ValueError('Agência inválida.')
        return True
    
    def __repr__(self) -> str:
        """Método de representação da classe."""
        return f'Banco {self.nome=}({self.clientes=}, {self.contas=}, {self.agencias=})'
