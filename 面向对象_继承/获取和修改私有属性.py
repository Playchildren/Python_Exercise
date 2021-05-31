"""
一般定义函数名 get_xx用来获取私有属性，定义set_xx用来修改私有属性值
其实就是在对应父类中添加两个函数分别获取和修改
"""


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

    def get_money(self):                # 获取 私有属性
        return self.__money

    def set_money(self):                # 修改 私有属性
        self.__money = input('你希望修改成：')


class practicer(School, Master):
    pass


daqiu = practicer()
print(daqiu.kongfu)
# print(daqiu.money)          # Error
daqiu.make_cake()
# daqiu.__i_have_money()      # Error
print(daqiu.get_money())
daqiu.set_money()
print(daqiu.get_money())
