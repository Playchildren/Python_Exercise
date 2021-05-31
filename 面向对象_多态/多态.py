"""
传入不同的对象，产生不同的结果
"""


class Dog(object):
    def work(self):
        print('指哪打哪。。。。。。')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人。。。。。。')


class DrugDog(Dog):
    def work(self):
        print('追查毒品。。。。。。')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


diren = ArmyDog()
dupin = DrugDog()
qiu = Person()
qiu.work_with_dog(dupin)
qiu.work_with_dog(diren)
