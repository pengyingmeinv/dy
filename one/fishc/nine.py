# -*-coding:utf-8 -*-

__author__ = 'pengying'
import sys
# count = 3
# passworld = 'good'
#
# while count:
# a = input(' Please enter your password：\n')
# if a == passworld:
# print('yes')
# break
# elif '*' in a:
# print('请输入正确字符')
# continue
# else:
# print('输入错误，你还有', count - 1, '次机会')
# count = count - 1

# for i in range(100, 1000):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp % 10) ** 3
#         temp //= 10
#     if sum == i:
#         print(i)
#
# print('red\tyello\tgreen')
# print('red\tyellow\tgreen')
# sum_list = []
# for red in range(0, 4):
#     for yellow in range(0, 4):
#         for green in range(2, 7):
#             su_list = []
#             if red + yellow + green == 8:
#                 # 注意，下边不是字符串拼接，因此不用“+”哦~ss
#                 #print(red, ' ', yellow, ' ', green)
#                 su_list.append(red)
#                 su_list.append(yellow)
#                 su_list.append(green)
#                 #print(su_list)
#                 sum_list.append(su_list)
# for x in sum_list:
#     print(x)
# #print(sum_list)
# print(len(sum_list))


name = ['a', 'b', 'c', 'd', 'e']
name.append(['o', 'i'])
name.extend(['k', 'l'])
name.insert(1, 'p')
print(name)
member = ['小田', 88, '小红', 85, '秋水', 95, '英男', 89, '心怡', 99]

count = 0
lenght = len(member)
while count < lenght:
    print(member[count], member[count + 1])
    count += 2

for x in range(len(member)):
    if x % 2 == 0:
        print(member[x], member[x + 1])

list1 = [1, 3, 2, 9, 7, 8]
print(list1[2:5])
print(list1[0])
print(list1[:])
print(list1.pop())

list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]
print(list1)
list2 = []
for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                list2.append([x, y])
print(list2)

# list2=[]
# list2.append(x)
# list2.append(y)
# print(list2)


# old = [1, 2, 3, 4, 5]
# new = old
# old = [6]
# print(new)

list3 = ['1.one', '2.tow', '3.three', '4.fron', '5five']
list4 = ['1', '2', '2', '4', '5']
list5 = [name + '' + zimu[2:] for zimu in list3 for name in list4 if zimu[0] == name[0]]
print(list5)
list6 = [name + slogan[2:] for slogan in list3 for name in list4 if slogan[0] == name[0]]
for d in list6:
    print(d)

s = 'helloWorld'
print(s)
a = s.capitalize()
print(s.capitalize())
print(a)
b = s.center(12, '*')
print(b)
e = s.count('llo')
print(s.upper())

g = '''1,
2
'''
h = 1, '\n', 3
print(g)
print(h)


def f(p, l):
    return p - l


print(f(5, 9))
print(int('1101', 2))
print(format(1.2345, '0.3f'))
s = 's,pa,m'
print(s.split(',')[1])
print(s[2:4])


print("{{1}}".format("不打印", "打印"))

# input('请输入一个整数（输入q结束程序）:')
# a = input()
# print(a)


l = [1, 2, 3]
l[:2] = []
print(l)


def power( x , y):
    result = 1

    for i in range(y):
        result *= x

    return result

print(power(2, 3))

#help(print())


var = ' Hi '

def fun1():
    global var
    var = ' Baby '
    return fun2(var)

def fun2(var):
    var += 'I love you'
    fun3(var)
    print(var)
    return var

def fun3(var):
    var = ' 小甲鱼 '
    return var
    #print(var)
h = 'hi,'
print(fun1())
print(fun2(h))
print(fun3(h))
#print(fun3())
