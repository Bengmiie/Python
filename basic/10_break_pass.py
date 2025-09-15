# import time
# running = True
# cup = 0
#
# while running:
#     cup += 1
#     print(cup)
#     time.sleep(0.5)
#     if cup == 10:
#         # running = False
#         break
#
# print('while 문 종료')
import time

for i in range(1,10):
    time.sleep(0.1)
    if i % 3 == 0:
        continue

    print(i)



