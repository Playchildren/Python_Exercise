"""
类属性是被所有类对象拥有的属性，可以使用类对象和实例对象访问
"""


class Dog(object):
    tooth = 10              # 类属性占用内存更少

wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
xiaohei.tooth = 20      # 通过实例对象修改，表示的是创建了一个实例属性
print(xiaohei.tooth)

Dog.tooth = 30          # 通过类对象修改，修改除了xiaohei之外的对象
print(Dog.tooth)

print(xiaohei.tooth)    # 因为xiaohei已经有了实例属性，因此不被类属性修改

print(wangcai.tooth)
