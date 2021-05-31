class Home():
    def __init__(self, Location, Area):
        self.Location = Location
        self.Area = Area
        self.remain_Area = Area
        self.furniture = []

    def add_Furniture(self, item):
        if self.remain_Area >= item.areas:
            self.furniture.append(item.name)
            self.remain_Area -= item.areas
        else:
            print('Error')

    def __str__(self):
        return f'房屋位置在{self.Location}，占地面积有{self.Area}，房屋剩余面积{self.remain_Area}，家具有{self.furniture}'


class Furniture():
    def __init__(self, name, areas):
        self.name = name
        self.areas = areas


MyHome = Home('Xian', 150)

FirstFur = Furniture('电脑', 200)
SecondFur = Furniture('沙发', 5)

MyHome.add_Furniture(SecondFur)
print(MyHome)

