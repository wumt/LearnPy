# coding=UTF-8
from collections import Iterable
import os
import functools
import Lession1
def my_fun():
    print isinstance(111, Iterable)
    for i, value in enumerate(['A', 'B', 'C']):
        print i, value
def __main__():
    my_fun()
    print range(1,10,2)

L = [x * x for x in range(10)]
print L
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1



def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn,map(char2num,'13579'))


def is_odd(n):
    return n%2==1
print filter(is_odd,[1,2,3,4,5,6,7,8,9,10])

print sorted([123,41,51,754,146,7,12,6,7,13])

intx=functools.partial(int , base=2);
print intx('11111000')


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')

@log
def alan():
    print('wo shi alan')
now()
alan()
Lession1.my_fun()