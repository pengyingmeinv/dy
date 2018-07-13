# -*-coding:utf-8 -*-
import requests
from one.weeked.weeked import ask_ok
__author__ = 'pengying'

def fib(num):
    """ fib func """
    a, b = 0, 1
    while b < num:
        print(b)
        a, b = b, b + a
    return
fib(2)


# def fib2(number):
#     result=[]
#     a,b=0,1
#     while b < number:
#         result.append(b)
#         a,b = b,a + b
#         print(result)
#     return result
# fib2(2)


s='Hello, world.'
print(s)
print(repr(s))  #加引号

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is '+repr(x)+',and y is '+repr(y)
print(s)

for x in range(1,11):
    print('{0:2d}{1:3d}{2:4d}'.format(x,x*x,x*x*x))
print('we are the {} who say "{}!"'.format('knights','ni'))

if __name__=="__main__":
    print(dir(requests))
    print(ask_ok("==>"))