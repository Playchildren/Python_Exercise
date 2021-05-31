def testA(a, b):
    print(a + b)


if __name__ == '__main__':  # 仅在本文件中执行的内容,调用import时不执行
    testA(2, 2)

# __name__是系统变量，是模块的标识符，值为
# 如果是自身模块，值是__main__，否则是当前模块的名字。
