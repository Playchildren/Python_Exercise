"""
父类代码在子类重新封装，优先执行子类的同名属性和方法
"""


class Master(object):
    def __init__(self):
        self.kongfu = '煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')


class School(object):
    def __init__(self):
        self.kongfu = '梅菜扣肉'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')


class practicer(School, Master):
    def __init__(self):
        self.kongfu = '独创'

    def make_cake(self):
        print(f'方法是{self.kongfu}')


daqiu = practicer()
print(daqiu.kongfu)
daqiu.make_cake()

"""
查看继承顺序
"""
print(practicer.__mro__)
