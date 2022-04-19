# imports
import time
from random import randrange


# 진행 함수
def intro():
    time.sleep(1)
    print(">>> 홀짝 게임 <<<")
    time.sleep(1)
    print("규칙: 주사위를 굴려서 나오는 수가 홀수일지 짝수일지 맞추시오.")
    print("")


def select():
    time.sleep(1)
    selection = input("홀수일까 짝수일까?   ")

    # validity checker
    count = 0
    while selection != "홀수" and selection != "짝수":
        time.sleep(0.5)

        if count >= 3:
            print("")
            print("게임 진행이 안되는 관계로 기권패 하겠습니다.")
            return 1

        if count == 2:
            print("")
            print("마지막 기회입니다.")
            time.sleep(0.5)
            selection = input("홀수, 짝수 중에 고르시오   ")
        else:
            selection = input("홀수, 짝수 중에 고르시오   ")

        count += 1

    return selection


def roll():
    return randrange(7)


def result(player, dice):
    time.sleep(1)

    # 히든 시나리오
    if player == 1:
        print("")
        print("")
        print("기권패하였습니다")
        return player

    # 승리 시나리오
    if (dice % 2 == 0 and player == "짝수") or (dice % 2 == 1 and player == "홀수"):
        print("")
        print("")
        print("승리!")
        print("====================")
        print("내 예측: ", player)
        print("주사위 결과: ", dice)
        print("====================")
        return 0

    # 패배 시나리오
    print("")
    print("")
    print("패배...")
    print("====================")
    print("내 예측: ", player)
    print("주사위 결과: ", dice)
    print("====================")
    return 1


def run():
    intro()
    result(select(), roll())


run()