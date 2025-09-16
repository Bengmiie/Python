
class Runner:
    def run(self):
        print('달린다.')

    def sprint(self):
        print('전력 질주를 한다')


class Jumper:
    def jump(self):
        print('점프를 한다')

    def high_jump(self):
        print('높이 점프를 한다')

class Person(Jumper, Runner):
    def walk(self):
        print('걷는다')

# walk()    함수를 사용하기 위해 Person 클래스를 객체화 한다.
p = Person()
p.walk()

# 상속받은 함수들을 내 것처럼(p객체로부터) 사용한다.
p.jump()
p.high_jump()
p.run()
p.sprint()
