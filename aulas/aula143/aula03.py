"""Parte 3 de multithreading"""

from threading import Thread
from time import sleep


def vai_demorar(texto: str, tempo: float) -> None:
    sleep(tempo)
    print(texto)


thread = Thread(target=vai_demorar, args=('Thread executada!', 10))
thread.start()

print('Esperando a conclusão da thread...')
while thread.is_alive():
    print('...')
    sleep(2)
