money = int(input("금액을 넣어주세요: "))
menu = {"콜라": 500, "커피": 400, "사이다": 300, "율무차": 200}
key = list(menu.keys())
value = list(menu.values())


def machine(money):
    print("[이화네 음료수]")
    print("현재 금액: %d 원" % (money))

    for i in range(4):
        print((i+1), ". ", key[i], " - ", value[i], "원")

    num = int(input("음료를 선택해주세요: "))
    return money - value[num-1]


while True:
    exchange = machine(money)
    if (exchange > 0):
        print("잔액은 %d원 입니다." % (exchange))
        choice = str(input("추가로 구매하시겠습니까?(Y/N): "))

        if (choice == 'Y'):
            money = exchange
            continue
        else:
            print("종료 선택! 이용해주셔서 감사합니다.")
            break

    elif (exchange == 0):
        print("잔액은 0원입니다. 이용해주셔서 감사합니다.")
        break

    else:
        print("금액이 부족합니다.")
        break
