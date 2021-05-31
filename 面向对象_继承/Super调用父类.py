class Master(object):
    def __init__(self):
        self.kongfu = '煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')


class School(Master):
    def __init__(self):
        self.kongfu = '梅菜扣肉'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')
        # Super新方法2.1：
        # Super(当前类名,self).函数()
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # Super 2.2
        # super().函数()
        # super().__init__()
        # super().make_cake()


class practicer(School):
    def __init__(self):
        self.kongfu = '独创'

    def make_cake(self):
        self.__init__()
        print(f'方法是{self.kongfu}')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 一次性调用两个父类
    def make_old_cake(self):
        # 旧方法1：
        School.__init__(self)
        School.make_cake(self)
        Master.__init__(self)
        Master.make_cake(self)

        # Super新方法2.1：
        # Super(当前类名,self).函数()
        # super(practicer, self).__init__()
        # super(practicer, self).make_cake()

        # Super 2.2
        # super().函数()
        # super().__init__()
        # super().make_cake()



daqiu = practicer()
daqiu.make_old_cake()

print(practicer.__mro__)

"""
super就是直用最近原则的mro顺序调用上层父类的相关函数
"""
