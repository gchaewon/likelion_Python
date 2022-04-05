import time
import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
# 리스트를 집합으로 바꾸기

while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])
# 집합을 이용한 리스트 삭제 반복문

print(set_lunch, "중에서 선택합니다.")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

random.choice(list(set_lunch))
print(random.choice(list(set_lunch)))
