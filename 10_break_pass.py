import time
running = True
cup = 0

while running:
    cup += 1
    print(cup)
    time.sleep(0.5)
    if cup == 10:
        # running = False
        break

print('while 문 종료')