"""
Introdução às Generator Functions em Python
    -> generator = (n for n in range(1000000))
"""


def generator(n=0, max=100):
    while True:
        yield n
        n += 1
        if n>= max:
            return
        

for n in generator(max=10):
    print(n)
