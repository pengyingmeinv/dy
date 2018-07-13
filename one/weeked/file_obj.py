# -*-coding:utf-8 -*-

__author__ = 'pengying'

import json
import requests
import os


import sys

'''
   w 写入
   r 读取
   a 添加
'''
# file = open('E:/pengying/one/weeked/test.log','w',encoding='utf-8')
# file.write('hello,world \n')
# file.write('good  day')
# file.close()
#

# with open('E:/pengying/one/weeked/test.log','r',encoding='utf-8') as file:
#     print(file.readlines())
#
# #os.remove('E:/pengying/one/weeked/test.log')
#
# content =requests.get('http://img.blog.csdn.net/20160125135944363').content
#
# #bytes 数据类型
# with open('E:/pengying/one/weeked/file/img.png','wb') as img:
#     img.write(content)
#
# # content = requests.get("http://124.202.166.51/file3.data.weipan.cn/57840318/ee19d3d13236345b0bc6ef534b4650d7faccd6e5?ip=1492468507,121.69.255.251&ssig=wMr1RswuwB&Expires=1492469107&KID=sae,l30zoo1wmz&fn=Python%20web%E6%A1%86%E6%9E%B6.Flask%E4%B8%AD%E6%96%87%E6%89%8B%E5%86%8C.pdf&skiprd=2&se_ip_debug=121.69.255.251&corp=2&from=1221134&wshc_tag=0&wsts_tag=58f53e6c&wsid_tag=e83151f&wsiphost=ipdbm").content
# # with open('E:/pengying/one/weeked/file/flask.pdf', 'wb') as pdf:
# #     pdf.write(content)
#
# _json={
#     "name":"ray",
#     "sex" :"male",
#     "age" :"22",
#     "like":"erevything"
# }
#
# with open('file/userinfo.json','w') as file:#json.dumps : dict转成str  json.dump是将python数据保存成json
#     json.dump(_json,file)  #将dict转成str
# with open('file/userinfo.json','r') as file:
#     print(json.loads(file.read()))  #json.loads:str转成dict    json.load是读取json数据
#

# while 1:
#     try:
#         user_input =int (input('plesase enter every number'));
#         break
#     except ValueError as ve:
#         print('Oops ! That was no valid number. Try again...')
#     except KeyboardInterrupt as kbi:
#         break
# try:
#     with open('file/userinfo.json','r') as file:
#         data =file.read()
#     print(json.loads(data))
# except Exception as ex:
#     print(data)
#     print(ex)

try:
    f = open('file/userinfo.json','r')
    s = f.readline()
    i = int(s)
except Exception as ex:
    print(ex)

# for arg in sys.argv[1:]:
#     try:
#         f =open(arg,'r')
#     except IOError:
#         print('cannot open',arg)
#     else:
#         print(arg,'has',len(f.readlines()),'lines')
#         f.close()