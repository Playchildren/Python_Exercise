"""
类方法： @classmethod标识某个函数为类方法
"""


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):         # 通常是操作私有类属性时和类属性配合使用
        return cls.__tooth


wangcai = Dog()
result = wangcai.get_tooth()
print(result)

"""
静态方法： @staticmethod 不需要传递类对象或实例对象，没有形参。     可以通过 实例对象和类对象去访问
取消不必要的参数传递，有利于减少内存消耗
"""


class Cat(object):

    @staticmethod
    def info_print():
        print(f'这是一个猫')


xiaomiao = Cat()
xiaomiao.info_print()
