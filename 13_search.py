# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
from operator import truediv

a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?: {a.index(2)}')
print(f'G는 어디?: {a.index('G')}') # G 는 2 개 이지만 처음 찾은 값만 알려준다.

# 5 번 인덱스 부터 'G' 를 찾아라
print(f'G는 어디?: {a.index('G',5)}')
# 값이 없으면 에러(예외)를 발생 시킨다.
# print(a.index('H')) # ValueError: 'H' is not in list

b = [3,4,1,2,3,4,5,6,1,3,2]  # 모든 3을 찾아 보세요
idx = 0                                # idx 에 숫자 0 을 대입한다
# while True:                       #
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx} 번에 있다.')
#     idx += 1

for n in b:
    if n == 3:
        print(f'{idx}')
    idx += 1