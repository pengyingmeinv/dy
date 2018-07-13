# -*-coding:utf-8 -*-

__author__ = 'pengying'
def ask_ok(prompt, retries=4, complaint='Yes or No, please!'):
    '''ask ok function'''
    while 1:
        # 1 可以代表true
        # 非空的字符串，非空的字典，非空的元祖和非空的数组。
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True;
        if ok in ('N','No','Nop','Nope'):
            return False;
        retries -= 1  #retries=retries-1
        if retries<0:
            raise IOError('uncooperative user')
            #    raise 抛出异常 IOError
        print(complaint)
interger = 5

def func(arg=interger):
    '''pass'''
    print(arg)

def function(number,_list=None):
    '''number append _list'''
    if _list is None:   # 如果进if 则代表_list的值==None
        _list = []
    _list.append(number)
    return  _list


def _parrot(*args,**kwargs):
    '''如果我们不确定这个函数需要接受多少个关键字和参数的时候，我们可以使用*args、**kwargs的是形式来接受位置的参数'''
    print('args:',args)
    print('kwargs',kwargs)


def parrot(voltage,state='a stiff',action='woom',type='Norwegian Blue'):
    '''pass'''
    print("This parrot wouldn't",action,'end=''')
    print("if you put",voltage,"volts throuhg it.")
    print("--Lovely plumage,the",type)
    print("--It's",state,"!")

def function(a):
    '''PASS'''
    pass

def cheeseshop(kind,*args,**kwargs):
    '''pass'''
    print('Do you have any',kind,"?")
    print("--I'm sorry,we're all out of",kind)
    for arg in args:
        print(arg)
    print("-"*40)
    keys =sorted(kwargs.keys())    # type(kwargs) == > dict, dict.keys()
    for kw in keys:
        print(kw,':',kwargs[kw]) #dict[key],dict.get(key)
parrot("jiubugaosuni1")