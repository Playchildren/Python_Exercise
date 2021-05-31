"""
特殊功能的函数
__init__():初始化对象
"""


# class Washer():
#     def __init__(self):         # 初始化所有对象的相关属性值
#         self.height = 800
#         self.weight = 500
#
#     def print_info(self):
#         print(f'The height is {self.height}')
#         print(f'The weight is {self.weight}')
#
#
# haier = Washer()
# haier.print_info()

"""
带参数的__Init__()  
对不同对象设置不同的初始化属性
"""


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'Width is {self.width}')
        print(f'Height is {self.height}')


haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(100, 200)
haier2.print_info()
