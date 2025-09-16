class Parent:
    def __init__(self):
        print('부모 생성자 실행')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print('자식 생성자')

ch = Child()


class SchoolMember:

    name = ''
    age = 0

    def __init__(self, name, age):
# 3. 받아온 값을 저번 시간에 배웠던 것 처럼 객체 멤버에 self. 를 달아 누가 값을 받을 것인지 지정하여 초기화 할 값을 넣는다
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    salary = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age)
# 2. 부모(super) 를 객체화 하며 초기화 할 값(name,age) 을 전달한다 *부모를 먼저 객채화 하는 이유* 순서상 부모가 자식보다 먼저 객채화 되어야 하기 때문
        self.salary = salary
# 4. 이 후 자식의 멤버 값을 초기화 하기 위해 값을 입력해 집어 넣는다

t = Teacher('김철수',33,5000000)
# 1. Teacher 라는 class를 객체화 시키며 상속 받을 멤버값(name,age)과  자신의 객체 멤버값(salary)을 초기화를 위해 매개변수에 넣어준다
print(f'{t.name}({t.age}) - {t.salary}')
# 5. 따라서 name 과 age 를 t.(객체화 한 Teacher) 를 통해서 상속받는다 (자신의 것이 아닌데 자신의 것처럼 쓸 수 있음) salary 는 내 객체이기 때문에 그냥 가져다 쓸 수 있다.

# SchoolMember 라는 부모의 객체 멤버인 name 과 age 를 Teacher 가 상속받으며 자신의 것처럼 사용 할 수 있게 함.