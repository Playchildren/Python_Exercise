"""
1. 出拳
    玩家：手动输入
    电脑：1.固定剪刀 2.随机
2.判断输赢
    2.1胜
    2.2平
    2.3负
"""


def number_random():
    import random
    print(random.randint(1, 3))


def if_play_program():
    player = int(input('你选择出拳（0--石头、1--剪刀、2--布）'))

    computer = 1

    if (player == 0) and (computer == 1):
        print('you win')
    elif player == computer:
        print('Equal')
    elif (player == 2) and (computer == 1):
        print('you lose')
    else:
        print('you give wrong input, restart')
        if_play_program()


def while_program():
    i = 0
    while i < 5:
        print('sorry')
        i += 1
    print('mission complete')


def add():
    i = 1
    result = 0
    while i < 101:
        result = result + i
        i += 1
    print(result)


def add1():
    i = 0
    result = 0
    while i < 101:
        if i % 2 == 0:
            result = result + i
        i += 1
    print(result)


def add2():
    i = 0
    result = 0
    while i < 101:
        result = result + i
        i += 2
    print(result)


def break_sentence():
    i = 1
    while i <= 5:
        print(f'Im eating {i} apple')
        if i == 3:
            print('i do not want more')
            break
        i += 1


def continue_sentence():
    i = 1
    while i <= 5:
        if i == 4:
            print(f'this {i} apple is bad')
            i += 1
            continue
        print(f'Im eating {i} apple')
        i += 1
