from student import *


class StudentManager(object):
    def __init__(self):
        # 存储数据所用列表
        self.student_list = []

        # 程序入口函数， 启动程序后，执行的函数
    def run(self):
        self.load_student()

        while True:

            self.show_menu()
            menu_num = int(input('请输入你需要的功能序号： '))

            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                print('退出系统')
                break

    @staticmethod
    def show_menu():
        print("""
        请选择如下功能：
        1.添加学员
        2.删除学员
        3.修改学员
        4.查询学员
        5.显示所有学员
        6.保存信息
        7.退出系统
        """)

    def add_student(self):
        print('----添加学员----')

        name = input('Your name is: ')
        gender = input('Your gender is: ')
        tel = input('Your tel is: ')

        new_student = Student(name, gender, tel)
        self.student_list.append(new_student)

    def del_student(self):
        print('----删除学员----')

        del_name = input('请输入要删除的学员姓名： ')

        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            # 循环正常结束后执行的代码：循环结束后都没有执行 if，表明没有这个人
            print('查无此人')

    def modify_student(self):
        print('----修改学员----')

        modify_name = input('请输入要修改的学员姓名： ')

        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('New name is：')
                i.gender = input('New gender is: ')
                i.tel = input('New tel is ')
                print(f'修改后的信息为：{i.name}, {i.gender}, {i.tel}')
                break
        else:
            print('查无此人')

    def search_student(self):
        print('----查找学员----')

        search_name = input('请输入要查找的学员姓名： ')

        for i in self.student_list:
            if i.name == search_name:
                print(f'您查找的信息为：姓名{i.name}, 性别{i.gender}, 电话{i.tel}')
                break
        else:
            print('查无此人')

    def show_student(self):
        print('----显示所有学员----')

        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        print('----保存学员信息----')

        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))

        f.close()

    def load_student(self):
        print('----加载学员信息----')

        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)       # 字符串还原成原本的列表类型
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()
