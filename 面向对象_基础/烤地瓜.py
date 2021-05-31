class Melon():
    def __init__(self):
        self.time = 0
        self.state = '生的'
        self.seasonings = []

    def cook(self, time):
        self.time += time
        if  0 <= self.time < 3:
            self.state = '生的'
        elif 3 <= self.time < 5:
            self.state = '半生不熟'
        elif 5 <= self.time < 8:
            self.state = '熟了'
        elif self.time >= 8:
            self.state = '烤糊了'

    def add_seasonings(self, seasonings):
        if  5 <= self.time < 8:
            self.seasonings.append(seasonings)
        else:
            print('地瓜不是熟了的状态，不能添加填料，请继续烤。')

    def __str__(self):
        return f'这个地瓜烤了{self.time}分钟，现在的状态是{self.state},调料是{self.seasonings}'


digua1 = Melon()
digua1.cook(4)
print(digua1)
digua1.add_seasonings('辣椒')
digua1.cook(3)
digua1.add_seasonings('胡椒')
print(digua1)
