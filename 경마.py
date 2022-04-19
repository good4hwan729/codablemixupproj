# imports
import time
from random import randrange


# 진행 함수
def intro():
    time.sleep(1)
    print(">>> 경마 게임 <<<")
    time.sleep(1)
    print("1등으로 들어올 말을 찾아라!")
    time.sleep(1)


def select():
    time.sleep(0.5)
    selection = int(input("1번부터 7번 중 몇번 말이 가장 먼저 들어올까?  "))

    # test for invalid input
    count = 0
    while selection not in range(1, 8):
        time.sleep(0.5)

        if count >= 3:
            print("")
            print("게임 진행이 안되는 관계로 기권패 하겠습니다.")
            return 0

        if count == 2:
            print("")
            print("마지막 기회입니다.")
            time.sleep(0.5)
            selection = int(input("1번부터 7번 중 몇번 말이 가장 먼저 들어올까?  "))
        else:
            selection = int(input("1번부터 7번 중 몇번 말이 가장 먼저 들어올까?  "))

        count += 1

    return selection


def blank(distance):
    to_return = ""

    for i in range(distance):
        to_return += " "

    return to_return


def gameboard(d1, d2, d3, d4, d5, d6, d7):
    time.sleep(1)
    winner = []
    lane = [d1, d2, d3, d4, d5, d6, d7]
    max_distance = max(d1, d2, d3, d4, d5, d6, d7)
    if max_distance >= 65:
        for i in range(7):
            if lane[i] == max_distance:
                winner.append(i+1)

    print("#####################################################################")
    print(blank(65 - d1), "🐎", blank(d1), " 1번 레인")
    print("")
    print(blank(65 - d2), "🐎", blank(d2), " 2번 레인")
    print("")
    print(blank(65 - d3), "🐎", blank(d3), " 3번 레인")
    print("")
    print(blank(65 - d4), "🐎", blank(d4), " 4번 레인")
    print("")
    print(blank(65 - d5), "🐎", blank(d5), " 5번 레인")
    print("")
    print(blank(65 - d6), "🐎", blank(d6), " 6번 레인")
    print("")
    print(blank(65 - d7), "🐎", blank(d7), " 7번 레인")
    print("#####################################################################")

    if len(winner) != 0:
        return winner
    return [0, d1, d2, d3, d4, d5, d6, d7]


def run():
    intro()
    selection = select()

    # 기권패 엔딩
    if selection == 0:
        print("")
        print("패배...")
        return 1

    case = gameboard(0, 0, 0, 0, 0, 0, 0)

    while len(case) == 8 and case[0] == 0:
        case = gameboard(randrange(9)+case[1], randrange(9)+case[2], randrange(9)+case[3], randrange(9)+case[4],
                         randrange(9)+case[5], randrange(9)+case[6], randrange(9)+case[7])

    # 승리
    if selection in case:
        print("")
        print("")
        print("승리!")
        print("")
        print("내 베팅: [", selection, "] 번 말 ")
        print("결과: ", case, " 번 말")
        return 0

    # 패배
    print("")
    print("")
    print("패배...")
    print("")
    print("내 베팅: [", selection, "] 번 말 ")
    print("결과: ", case, " 번 말")
    return 1

run()
