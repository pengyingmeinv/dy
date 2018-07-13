# -*-coding:utf-8 -*-

__author__ = 'pengying'
import sys
import os
import re

print(sys.platform)  # platform 平台
print(2 ** 10)
x = 'Spam'
print(x * 8)
print(os.getcwd())  # 当前路径
# input('请输入')
line = 'aa,bbb,ccc,dd，cc\n'
print(line.rstrip('cc'))
line = line.rstrip()  # rstrip，删除指定字符串，不指定字符串默认删除最右边的空格或者转义符
print(line)

theString = 'saaaay yes no yaaaass'  # Python中的strip用于去除字符串的首尾字符，同理，lstrip用于去除左边的字符，rstrip用于去除右边的字符。

# 这三个函数都可传入一个参数，指定要去除的首尾字符。

print(theString.rstrip('say'))
print(theString.strip('say '))
macth = re.match('hello[\t]*(.*)world', 'hello python  world')
print(macth)
print(macth.group(1))

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = [sum(row) for row in m]
print(s)
g = (sum(row) for row in m)
print(g)
print(next(g))
# d={sum(row) for row in m}
# print(d)

# print({i:sum(m[i]) for i in range(3)})
#
#
# print([ord(x) for x in 'spssm'])#ord函数：为序数函数,函数返回值为字符在ASCII码中的序号.

squares = []
for x in [1, 2, 3]:
    squares.append(x ** 2)
    print(squares)


