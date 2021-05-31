class Master(object):
    def __init__(self):
        self.kongfu = '煎饼果子'

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')


class School(object):
    def __init__(self):
        self.kongfu = '梅菜扣肉'
        self.__money = '2000'           # 私有属性前面加两个下划线, 子类无法访问

    def make_cake(self):
        print(f'运用{self.kongfu}做果子')

    def __i_have_money(self):             # 私有方法前面加两个下划线，子类无法继承
        print('i have money')


class practicer(School, Master):
    pass


daqiu = practicer()
print(daqiu.kongfu)
# print(daqiu.money)          # Error
daqiu.make_cake()
# daqiu.__i_have_money()      # Error
