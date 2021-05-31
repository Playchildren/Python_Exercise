"""
While 循环嵌套语句
"""


def print_zhengfengxing():
    j = 0
    while j < 5:
        i = 0
        while i < 5:
            print('*', end='')
            i += 1
        print('')
        j += 1


def print_sanjiaoxing():
    j = 0
    while j < 5:
        i = 0
        while i <= j:
            print('*', end='')
            i += 1
        print('')
        j += 1


for a in 'hello':
    print(a)


for a in 'hello':
    if a == 'e':
        break
    print(a)

for a in 'hello':
    if a == 'e':
        continue
    print(a)


"""
While else: while 正常退出后执行else，否则不执行
break不执行，continue执行 
For else: For 正常退出后执行else，否则不执行
break不执行，continue执行 
"""

name = 'Tom'
print("%s" % name)
print(f'{name[0]}')
