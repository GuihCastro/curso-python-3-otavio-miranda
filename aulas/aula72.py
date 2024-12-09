"""
Yield from
"""


def gen1():
    yield 1
    yield 2
    yield 3
    
    
def gen2(gen=None, arg=None):
    if gen:
        yield from gen(arg) if arg else gen()
    yield 4
    yield 5
    yield 6
    
    
def gen3(gen=None, arg=None):
    if gen:
        yield from gen(arg) if arg else gen()
    yield 666
    
    
for i in gen2(gen1):
    print(i)
    
print()
for i in gen3(gen2, gen1):
    print(i)
    
print()
for i in gen3():
    print(i)
