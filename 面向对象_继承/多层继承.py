"""
N 年后 daqiu老了 要把所有技术传承给徒弟（大于两层的继承关系）
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
        self.__init__()                     # 如果先执行父类的属性，self会被替换为父类的，因此重新调用子类self时需要初始化
        print(f'方法是{self.kongfu}')

    # 制作师傅传授的
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 制作学校传授的
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(practicer):
    pass


xiaoqiu = Tusun()
xiaoqiu.make_cake()
print(xiaoqiu.kongfu)
xiaoqiu.make_master_cake()
print(xiaoqiu.kongfu)


"""
查看继承顺序
"""
print(practicer.__mro__)
