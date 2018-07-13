# -*-coding:utf-8 -*-

__author__ = 'pengying'
from PIL import Image

#Gray = R*0.299 + G*0.587+B*0.114

codelib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''
count = len(codelib)


def transforml(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数l表示黑白模式
    codepic=''
    for h in range(0,image_file.size[1]): #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0, image_file.size[0]):
            gray = image_file.getpixel((w,h))#返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codepic = codepic + codelib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codepic =codepic+'\r\n'
    return codepic


fp = open(u'a.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.75), int(image_file.size[1]*0.5)))#调整图片大小
print (u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)
tmp = open('peter.txt','w')
tmp.write(transforml(image_file))
tmp.close()


