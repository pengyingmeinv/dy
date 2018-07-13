# -*-coding:utf-8 -*-
import math
# import types
import random
# import decimal
import copy

# from fractions import Fraction  # 分数
#
# __author__ = 'pengying'
#
#
# def a():
# x = ['女1', '女2', '女3', '女4']
# y = ['男1', '男2', '男3', '男5']
# r = ['吃饭', '看电影', '逛街', '聊天', '周边游一天', '其他']
#     print(type(x))
#     if (x.__len__() == y.__len__()):
#         c = random.sample(x, 1)
#         b = random.sample(y, 1)
#         return (c, b, random.sample(r, 1))
#     else:
#         pass
#
#
# print(a())
#
# d = {'a': 1, 'c': 2, 'b': 3, 'f': 4}
# value = d.get('x', 0)
# print(value)
# print(d)
#
# f = open('E:/pengying/one/weeked/file/test.txt', 'w')
# f.write('hello\n')
# f.write('wrold')
# f = open('E:/pengying/one/weeked/file/test.txt')
#
# r = f.read()
# print(r)
# print(r.split())
# print(dir(f))
#
# help(f.seek)
# x = set('spam')
# y = {'h', 'a', 'm'}
# print(x, y)
# print(x & y)
# print(x | y)
#
# d = decimal.Decimal('3.141')
# print(d + 1)
#
# f = Fraction(2, 3)  # 2/3 三分之二
# print(f + 1)
#

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):  # percent 百分比
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)

print(math.floor(2.5))
print(math.floor(-2.5))

x = 1
print(x << 2)
print(math.pi)
print(math.e)
print(pow(2, 4))  # pow(x,y) x**y
print(math.sqrt(144))  # math.sqrt  开方
print(abs(-42))  # 绝对值
print(math.trunc(3.14))  # 截取整数部分
print(0.1 + 0.1 + 0.1 - 0.3)

x = 3
y = copy.copy(x)
print(y)
a = [1, 2, 3, 4, ['a', 'a']]  # 原始对象
b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  #
a.append(5)
a[4].append('c')
print('a =', a)
print('b =', b)
print('c=', c)
print('d=', d)
5 + 8
print((5 + 8))

first = 520
second = '520'
first = second
print(first)
print(type(first))
range(1,5)

# while '':
#     print('进入循环')
# print('退出循环')

######按
# time = 3
# secret = random.randint(1, 10)  # 从1-10中随机获取一个数  # secret秘密
# # 给guess赋值
# guess = 0
# # print()默认打印完之后换行，end=''参数告诉print用空格代替换行
# print('你猜我在想几:', end="")
# while (guess != secret) and (time > 0):
#     tmp = input('\n')  # 输入一个数
#
#     if tmp.isdigit():
#         guess = int(tmp)
#         if (guess == secret):
#             print('答对了')
#         else:
#             if guess > secret:
#                 print('大了')
#             else:
#                 print('小了')
#             if time > 0:
#                 print('再来一次咯:', end='')
#             else:
#                 print('没有机会了')
#     else:
#         print('输入有误，请重新输入',end='')
#     time = time - 1  # 输入一次，次数减一
# print('gameover')
# import random
#
# times = 3
# secret = random.randint(1,10)
#
# print('------------------我爱鱼C工作室------------------')
# guess = 0
# print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
#
# while (guess != secret) and (times > 0):
#     temp = input()
#
#     if temp.isdigit():
#         guess = int(temp)
#         if guess == secret:
#             print("我草，你是小甲鱼心里的蛔虫吗？！")
#             print("哼，猜中了也没有奖励！")
#         else:
#             if guess > secret:
#                 print("哥，大了大了~~~")
#             else:
#                 print("嘿，小了，小了~~~")
#             if times > 1:
#                 print("再试一次吧：", end='')
#             else:
#                 print("机会用光咯T_T")
#     else:
#         print("抱歉，您的输入有误，请输入一个整数：", end='')
#
#     times = times - 1 # 用户每输入一次，可用机会就-1
#
# print("游戏结束，不玩啦^_^")

# temp = input('请输入一个整数:')
# number = int(temp)
# while number:
#     i = number - 1
#     while i:
#         print(' ', end = '')
#         i = i - 1
#     j = number
#     while j:
#         print('*', end = '')
#         j = j - 1
#     print()
#     number = number - 1

# temp =input('请输入')
# number=int(temp)
# i = 1
# while number:
#     print(i)
#     i=i+1
#     number = number -1

# temp=input('年份')
# years=int(temp)
# if years/4==0 and years/100!=0:
#     print('闰年')
# elif years/400==0:
#     print('runnian')
# else:
#     print('false')


while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)

for i in range(0, 10, 2):
    print(i)


count = 3
passworld = 'pengying.com'
while count:
    passw = input()