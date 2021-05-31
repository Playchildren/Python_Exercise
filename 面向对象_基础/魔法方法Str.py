"""
一般情况下打印对象名时，返回地址，如果定义了str，返回str中return的数据
"""


class Washer():
    def __init__(self, weight, width):
        self.weight = weight
        self.width = width
        print(f'{self}')

    def __str__(self):
        return '这是一台haier的洗衣机'  # 通常放置解释说明文字


haier = Washer(10, 20)
