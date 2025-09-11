# 파스칼 표기법 - 맨 앞글자만 대문자(Java의 Class 생성시 활용)
# 카멜 표기법 - 단어의 의미가 있는 첫글자를 대문자로 한다. (shopList)
# 스네이크 표기법 - 단어간의 구분을_로 한다.(shop_List)

# List 생성방법 1 - 비어있는 리스트로 생성
a = []

# list 생성방법 2 = 값이있는 리스트로 생성
shop_list = ['apple','mango','carrot','banana']
print(f'shop_list: {shop_list}')

# List 에 값을 넣는 방법
# 가장뒤로부터 넣는 방법
a.append(1)
a.append(2)
a.append(3)
# 특정한 번호를 지정해서 넣는 방법
a.insert(1,'X')

print(f'a 의 길이 : {len(a)}')
print(f'a : {a}')
# a 의 2번방에 있는 값
print(f'a[2] = {a[2]}')
# a 의 가장 마지막 방에 있는 값
print(f'a[의 가장 마지막] = {a[3]}')
# 길이에서 1을 뺀 값을 이용 -> 인덱스는 0 번부터 시작한다는 점을 이용
print(f'a[의 가장 마지막] = {a[len(a)-1]}')
# 팡리썬에서 사용되는 방식, 0 보다 디로가면 맨 뒤로 이동된다는 개념
print(f'a[의 가장 마지막] = {a[-1]}')