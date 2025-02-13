"""Módulo principal do programa."""

from banco import Banco
from contas import TipoConta

if __name__ == '__main__':
    try:
        banco = Banco('Banco Camarada')
        cliente1 = banco.cadastrar_cliente('Guilherme', 32)
        banco.adicionar_conta(cliente1, TipoConta.CORRENTE, 1111)
        cliente2 = banco.cadastrar_cliente('Mariana', 32)
        banco.adicionar_conta(cliente2, TipoConta.CORRENTE, 1111)
        cliente1.contas[0].depositar(1000)
        cliente2.contas[0].depositar(1000)
        cliente1.contas[0].sacar(1250)
        cliente2.contas[0].sacar(1250)
    except Exception as e:
        print('Erro:', e)
