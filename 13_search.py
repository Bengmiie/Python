# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
# from operator import truediv

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
# while True:                       # while 문을 강제로 True 로 설정해서 작동시킨다 (반복문)
#     idx = b.index(3,idx)      #
#     print(f'3의 값은 {idx} 번에 있다.')
#     idx += 1

for n in b:
    if n == 3:
        print(f'{idx}')
    idx += 1

# List 요소 삭제
# del a[3] 과 a.remove(3)
# del 은 특정 인덱스의 값을 지운다.
# remove 는 해당 값을 지운다.(한 개만)

print(a)
del a[3]
print(a)
a.remove(3)
print(a)

# pop() = append() 의 반대개념
# 맨마지막 요소를 빼낸다.(List에서는 사라진다.)
val = a.pop()
print(f'빼낸값 : {val} / a: {a}')
val = a.pop()
print(f'빼낸값 : {val} / a: {a}')

# List 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

# count(val) 특정한 값이 해당 리스트에 몇 개 있는지 확인.
print(a)
print(f'a 안에 3은 {a.count(3)}개 가 있다.')
print(f'a 안에 9는 {a.count(9)}개 가 있다.') # 없는 값은 0을 반환

# a 안에 있는 모든 3을 지워주세요
# a 에 있는 3 지우기, 못찾을 때 까지? 갯수가 0 개 일 때 까지?

# print(a)
# for d in a:
#     if d == 3:
#         a.remove(3)
# print(a)

while True:
    a.remove(3)
    if a.count(3) == 0:
        break
print(a)


