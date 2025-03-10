"""Threads - Executando processos em paralelo com o módulo `threading`"""

from threading import Thread
from time import sleep


class MeuThread(Thread):
    def __init__(self, texto: str, tempo:  float) -> None:
        self.texto = texto
        self.tempo = tempo

        Thread.__init__(self)

    def run(self) -> None:
        sleep(self.tempo)
        print(self.texto)


thread1 = MeuThread('Thread 1', 3.5)
thread2 = MeuThread('Thread 2', 5.5)
thread3 = MeuThread('Thread 3', 2.5)

thread1.start()
thread2.start()
thread3.start()

for i in range(10):
    print(i+1)
    sleep(1)

print('FIM!')
