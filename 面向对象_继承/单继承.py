"""
一个子类只继承一个父类
"""
class Master(object):
    def __init__(self):
        self.kongfu = '煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')


class practicer(Master):
    pass


Qin = practicer()
print(Qin.kongfu)
Qin.make_cake()
