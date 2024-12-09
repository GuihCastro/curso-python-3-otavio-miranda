"""
Iterables e Iterators em Python
"""

iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # iter(iterable) | tem __iter__ e __next__

print(iterator.__next__())
print(next(iterator))
print(iterator.__next__())
print(next(iterator)) # exceção StopIteration
