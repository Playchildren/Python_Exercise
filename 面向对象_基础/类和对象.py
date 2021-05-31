# use CLASS to create an OBJECT
class Washer():                            # 创建类, 遵循大驼峰命名习惯
    def wash(self):                        # 按照图纸，应该有这些功能
        print('washing machine')
        print(self)                        # self是指调用该函数的对象（是谁调用的函数，谁就是self）

    def cloth(self):
        print(f'height is {self.height}')  # 类里面获取对象属性


haier1 = Washer()                          # 创建对象（图纸造出来的第一个机器），拥有类的所有属性和方法
print(haier1)

haier1.wash()                              # 某个功能在特定机器(对象)里的实现

haier2 = Washer()
print(haier2)

haier2.wash()

"""
添加和获取对象属性
"""
# outside set
haier1.height = 800
haier1.weight = 500

haier2.height = 80
haier2.weight = 50

# get
print(haier1.height)

# inside get
# 类里面获取对象属性
haier2.cloth()
