import oper as op

# dir() 내장함수를 사용하면 모듈에 정의되어있는 변수, 함수 목록을 볼 수 있다.
print(dir(op))

#모듈의 이름 확인
print(op.__name__) # 특정 모듈의 이름 확인
print(__name__) # 현재 나의 이름 -> 현재 실행되는 함수