# 自定义异常类，继承Exception
class short_input_error(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

# 设置异常的描述信息
    def __str__(self):
        return f'the length you input is {self.length}, in can not less than {self.min_len}'


def main():
    try:
        con = input('your password: ')
        if len(con) < 3:
            raise short_input_error(len(con), 3)        # 抛出异常类对象
    except Exception as result:                         # 捕获异常
        print(result)
    else:
        print('already down')


main()
