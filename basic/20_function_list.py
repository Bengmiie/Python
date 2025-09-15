# 반환타입:O 매개변수:O    지도앱
def 매표소(돈):
    print(f'{돈}원 을 냈다 ')
    return f'입장권을 받았다 '

money = 매표소(1000)
print(money)

# 반환타입:O 매개변수:X     체중계
def 체중측정(체중):
    print('체중계에 올라갔다')
    return f'{체중}kg'

print(체중측정(60))

# 반환타입:X 매개변수:O     오락실
def 오락실(coin):
    return (f'{coin} 판 가능 ')

coin = 오락실(5)

# 반환타입:X 매개변수:X     초인종
def 초인종():
    print('띵동')

초인종()