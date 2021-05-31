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


daqiu = practicer()

daqiu.make_school_cake()                # 运用梅菜扣肉做果子
print(daqiu.kongfu)                     # 梅菜扣肉(父类的self直接覆盖子类的self)

# daqiu = practicer()
# print(daqiu.kongfu)                 # 独创
# daqiu.make_school_cake()            # 运用梅菜扣肉做果子

daqiu.make_cake()
print(daqiu.kongfu)


"""
查看继承顺序
"""
print(practicer.__mro__)
