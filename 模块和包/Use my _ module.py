import my_module1

my_module1.testA(1, 2)

# 导入模块时，优先搜素当前目录
# 然后搜 shell变量pythonpath下的每个目录
# 最后查看默认路径

# 不要重名定义模块，否则无法使用
# from import时，如果功能名字重复，会调用最后定义或导入的功能，会出错。
