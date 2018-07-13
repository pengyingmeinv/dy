# -*-coding:utf-8 -*-

# __author__ = 'pengying'
#

class MyClass:
    '''pass'''
    pass


class Student:
    '''pass'''
    metho = 'post'

    def __init__(self, name, score):  # 刚刚名字错了  你是  int
        '''pass'''
        self.__name = name
        self.name=name
        self.__score = score
        self.score=score

    def get_score(self):
        '''pass'''
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        '''pass'''
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


class StaticDemo:
    '''pass'''

    @staticmethod
    def simple():
        '''pass'''
        print('this is StaticDemo Class simple :')


class ClassMethodDemo:
    '''pass'''

    @classmethod
    def simple(cls):
        '''pass'''
        print('this is Class methodDemo class simple')


class NewStedent:
    '''the new student class'''

    def __init__(self, name, age):
        """ 该init方法为类方法中的构造函数，在实例化类的时候将在此方法下定义的类属性进行初始化"""
        self.name = name
        self.age = age

    def print_score(self):
        print('NewStudeng "s funtion %s:%s' % (self.name, self.age))
        return self.name, self.age


new_student = NewStedent('狗子', '5')
print(new_student)
print(new_student.name, new_student.age)


def print_name_and_age(std):
    '''pass'''
    print('%s:%s' % (std.name, std.age))


def scope_test():
    def do_local():
        spam = 'local spam'  # local  局部

    def do_nonlocal():
        nonlocal spam  # nonlocal外部
        spam = 'this is a nonlocal spam'

    def do_global():
        global spam
        spam = 'this is a global spam'

    spam = "test spam"
    do_local()
    print('After local assignment：', spam)  # assignment分配
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment:', spam)


if __name__ == '__main__':
    new_student.print_score()
    bart = Student('Bar Simpson', 59)

    print('bart.name=', bart.name)
    print('bert.score=,',bart.score)




