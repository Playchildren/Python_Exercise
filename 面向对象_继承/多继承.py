"""
一个子类继承多个父类
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


class practicer(School, Master):        # 默认继承第一个父类的同名属性和方法
    pass


Qin = practicer()
print(Qin.kongfu)
Qin.make_cake()
