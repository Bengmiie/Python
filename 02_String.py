# 문자열은 '' 나 "" 모두 사용 가능
name='kim baek min'
content = "My content"

# 여러줄의 문자열을 변수에 담을때
multi = '''this is multi line string
         this is second line'''

print('name:' +name)
print('content:' +content)
print('multi:'+multi)

# 문자열에 다른 타입의 데이터를 함께 출력 할 경우...
age = 23

print('내 이름은 {0} 이고, 나이는 {1} 입니다.'.format(name,age))   # format 문
print('내 이름은' + name + '이고 나이는' + str(age) + '입니다.')                  # str 함수 문
print(f'내 이름은 {name} 이고, 나이는 {age} 입니다.')                                # f 스트링 문

# 여러 줄 -> 한 줄로 처리, 한 줄 -> 여러 줄처럼 줄바꿈
print('이것은 한 줄 이지만\n 여러 줄 처럼 보이게 할 겁니다')
print('이것은 두 줄 이지만 \
한 줄 처럼 보이게 할 겁니다')