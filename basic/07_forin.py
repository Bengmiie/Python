# for 문은 반복 횟수가 정해진 상태에 적합하다.

# 물 10잔 떠오기
#for [하나씩 가져올 변수] in [범위]
for cup in range(1, 11):                            #
    print(f'물 {cup} 번째 잔 떠왔습니다.')
    for mix in range(1, 3):
        print(f'믹스를 {mix} 번 넣었다')
        for spoon in range(1, 4):
            print(f'{spoon} 번 스푼으로 젓는다.')

print()
# 만약 커피를 타는데 한잔의 물에 믹스 2개 씩을 넣어야 한다면?
# 반복안에 반복이 발생된다.