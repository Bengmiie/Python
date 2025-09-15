import random

number = random.randint(1,31) # 1~30 까지의 정수 값을 number 에 대입
print(f' 내 마음속 숫자: {number}')         # number 에 대입 된 정수 값을 표시
running = True                                     # running 을 True 로 바꿔 while 문을 작동시킨다

# guess = 입력받은 숫자
# number = 내 마음속 숫자

while running:                                                       # running 이 True 이기 때문에 while 문이 작동된다
    guess = int(input('1~30 까지 숫자를 입력 하세요'))# 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    print(f'입력받은 숫자: {guess}')                           # guess 에 대입 된 숫자 표시
    if guess>number:                                             # guess 에 대입 된 숫자가 number 보다 클 경우
        print('마음속 숫자보다 큽니다')                          # guess 가 number 보다 크다고 알려줌
    elif guess<number:                                          # guess 에 대입 된 숫자가 number 보다 작을 경우
        print('마음속 숫자보다 작습니다')                       # guess 가 number 보다 작다고 알려줌
    else:                                                               # guess 가 number 보다 크지도 작지도 않을 경우 ( 일치 할 경우 )
        print('정답')                                                  # guess 와 number 가 일치하다고 알려줌
        running = False                                            # running 을 False 로 바꿔 while 문을 끝내준다