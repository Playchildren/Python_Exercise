class Washer():
    def __init__(self, weight, width):
        self.weight = weight
        self.width = width

    def __del__(self):          # 运行结束后自动调用
        print(f'{self}对象已经删除')


haier = Washer(10, 20)

print(haier)
