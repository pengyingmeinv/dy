
# -*-coding:utf-8 -*-

__author__ = 'pengying'
print(2**16)
print(2/5)
print(2/5.0)
print('spam' + 'eggs')
s = 'ham'
print(s + 'hi')
print(s * 5)
a = s[:3]
print(a)
print(('x', 'z', 'y')[2])
l = [1, 2, 3] + [4, 5, 6]
print(l)

print(([1, 2, 3] + [4, 5, 6])[2:4])

d = {'x': 1, 'y': 2, 'z': 3}
print(d)
d['w'] = 0
print(d)
d[(1, 2, 3)] = 0
print(d)
print(list(d.keys()), list(d.values()), (1, 2, 3) in d)
print([[]], ["", [], (), {}, None])

print(l[-100:100])
print(l[3:1])
p = [1, 2, 3, 4]
p[2] = []
p[2:3] = []
o = [7, 8, 9]
del p[1:]
p[1:] = [2, 3, 4]
print(p)

# 元祖赋值
x = ['s', 'p', 'a', 'm']
print(x[0][0][0][0][0])
y = 'eggs'
li = list(y)
li[0] = 's'
li[1] = 'l'
print(li)
str1 = ''.join(li)
print(str1)
str2 = 'sl' + y[2:]
print(str2)
# x, y = y, x
# print(x, y)
# c = {}
# c[1] = 'a'
# c[2] = 'b'
# print(c)
# c['i'] = 'spam'
# print(c['i'])
# print(c)
# # print(s + l)
# f = (1, 2, 3)
# print(l+o)

info = {'name': ('颖', '爱', '彭'), 'age': 18, 'job': 'tester', 'address': 'Shenzhen', 'email': '269242530@qq.com', 'tel': 13197086722 }
print(info['name'][0])


# file

fp = open('myfile.txt', 'w')
fp.write('hello file world')
fp.close
fp = open('myfile.txt', 'r')
re = fp.read()
print(re)

# loop
# while True:
#     reply = input('text is:''\n')
#     if reply == 'stop':
#         break
#     try:
#         num = int(reply)
#     except:
#         print('bad' * 8)
#     else:
#         print(int(reply)**2)
# print('by')

# a, *b = 'spam'
# print(b)
string = 'spam'
c = list(string[:2]) + [string[2:]]
print(list(string[:2]))
i, k = list(string[:2])
# r, t, y = list(string[:2]) + [string[2:]]
# print(r, t, y)
# print(c)
# # a, b, d = c
# # print(a, b, d)
for i in range(3):
    print(i)
print()
j = '''
aaaa
bbbb
cccc
dddd
'''
print(j)


x = [1, 2, 3, 4]
[i+i for i in x];
print(x)
