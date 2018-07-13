
# -*-coding:utf-8 -*-

__author__ = 'pengying'
# def palindrome(string):
#     lenght = len(string)
#     last = lenght-1
#     lenght //= 2
#     flag = 1
#     for each in range(lenght):
#         if string[each] != string[last]:
#             flag = 0
#         last -= 1
#
#     if flag == 1:
#         return 1
#     else:
#         return 0
# string = input("请输入一个：")
#
# if palindrome(string)==1:
#     print('是回文联')
# else:
#     print('不是回文联')


def count(*param):
    lenght = len(param)
    for i in range(lenght):
        letters = 0 #字母
        sapce = 0 #空格符
        digit = 0 #数字
        other = 0
        for ecah in param[i]:
            if ecah.isalpha(): # isalpha() 方法检测字符串是否只由字母组成
                letters += 1
            elif ecah.isspace():
                sapce += 1
            elif ecah.isdigit(): #isdigit() 所有字符都是数字
                digit += 1
            else:
                other += 1
        print('第%d字符串，共有英文字母%d个，数字%d个，空格%d个，其他字符%d个' % (i+1, letters, digit, sapce, other))
        print(('第{}字符串，共有英文字母{}个，数字{}个，空格{}个，其他字符{}个').format(i+1, letters, digit, sapce, other))
count('i love you 1314', 'I love you, you love me.')

# def count(*param):
#     length = len(param)
#     for i in range(length):
#         letters = 0
#         space = 0
#         digit = 0
#         others = 0
#         for each in param[i]:
#             if each.isalpha():
#                 letters += 1
#             elif each.isdigit():
#                 digit += 1
#             elif each == ' ':
#                 space += 1
#             else:
#                 others += 1
#         print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i+1, letters, digit, space, others))

#
# count('I love fishc.com.', 'I love you, you love me.')
