"""Parte 4 de multithreading"""

from threading import Lock, Thread
from time import sleep


class Ingressos:
    def __init__(self, estoque: int) -> None:
        self._estoque = estoque
        self.lock = Lock()

    @property
    def estoque(self) -> int:
        return self._estoque

    @estoque.setter
    def estoque(self, valor: int) -> None:
        # if valor < 0:
        #     raise ValueError('Estoque não pode ser negativo.')
        self._estoque = valor

    def comprar(self, quantidade: int) -> None:
        self.lock.acquire()
        if quantidade > self.estoque:
            # raise ValueError('Estoque insuficiente.')
            print('Estoque insuficiente.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Compra de {quantidade} ingressos realizada com sucesso.'
              f' Restam {self.estoque} em estoque.')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(15):
        Thread(target=ingressos.comprar, args=(i+1,)).start()
        # ingressos.comprar(i+1)
