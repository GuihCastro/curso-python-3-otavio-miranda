"""Parte 2 de multithreading"""

from threading import Thread
from time import sleep


def vai_demorar(texto: str, tempo: float) -> None:
    sleep(tempo)
    print(texto)
    
    
thread1 = Thread(target=vai_demorar, args=('Thread 1 executada!', 7.5))
thread2 = Thread(target=vai_demorar, args=('Thread 2 executada!', 2.5))
thread3 = Thread(target=vai_demorar, args=('Thread 3 executada!', 5))

thread1.start()
thread2.start()
thread3.start()

for i in range(20):
    print(i+1)
    sleep(.5)
    
print('FIM!')
