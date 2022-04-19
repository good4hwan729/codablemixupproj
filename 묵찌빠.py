# imports
import time
from random import randrange


# 진행 함수
def intro():
    time.sleep(1)
    print('>>> 묵찌빠 게임! <<<')
    time.sleep(1)
    print('이번 게임은 묵찌빠입니다.')
    time.sleep(1)


def player_select():
    print("")
    print("")
    print("#######################")
    print("")
    selection = input("묵, 찌, 빠 셋 중 무얼 낼까?  ")

    # test for invalid input
    count = 0
    while selection != "묵" and selection != "찌" and selection != "빠":
        time.sleep(0.5)

        if count >= 3:
            print("")
            print("게임 진행이 안되는 관계로 기권패 하겠습니다.")
            return 1

        if count == 2:
            print("")
            print("마지막 기회입니다.")
            time.sleep(0.5)
            selection = input("묵, 찌, 빠 중에서 하나를 고르세요.  ")
        else:
            selection = input("묵, 찌, 빠 중에서 하나를 고르세요.  ")

        count += 1

    return selection


def com_select():
    selection_list = ["묵", "찌", "빠"]

    return selection_list[randrange(99) % 3]


def init_attack(p, c, initial):
    while p == c:
        time.sleep(0.5)
        result(p, c)
        print("이런! 상대랑 같은걸 냈다...")
        c = com_select()
        p = player_select()

    if initial == 0:
        result(p, c)

    time.sleep(0.5)
    if p == "묵":
        if c == "찌":
            print("아싸! 내 선공이다!")
            return [0, p, c]
        if c == "빠":
            print("상대 선공이네...")
            return [1, p, c]
    elif p == "찌":
        if c == "빠":
            print("아싸! 내 선공이다!")
            return [0, p, c]
        if c == "묵":
            print("상대 선공이네...")
            return [1, p, c]
    else:
        if c == "묵":
            print("아싸! 내 선공이다!")
            return [0, p, c]
        if c == "찌":
            print("상대 선공이네...")
            return [1, p, c]


def result(player, com):
    print("")
    print("====================")
    print("나: ", player)
    print("상대: ", com)
    print("====================")
    print("")


def attack(attacking, cur_player, cur_com, player_selection, com_selection):
    if attacking == 2 or attacking == 3:
        return [attacking, 0, 0]

    # 플레이어 공격
    if attacking == 0:
        time.sleep(1)
        print(cur_player, "...")
        time.sleep(1)
        print(cur_player, "...")
        time.sleep(1)
        print(player_selection, "!!!")
        result(player_selection, com_selection)

        if player_selection == com_selection:
            return [2, 0, 0]
        c = init_attack(player_selection, com_selection, 1)
        return [c[0], c[1], c[2]]

    # 컴퓨터 공격
    time.sleep(1)
    print(cur_com, "...")
    time.sleep(1)
    print(cur_com, "...")
    time.sleep(1)
    print(com_selection, "!!!")
    result(player_selection, com_selection)

    if player_selection == com_selection:
        return [3, 0, 0]
    c = init_attack(player_selection, com_selection, 1)
    return [c[0], c[1], c[2]]


def run():
    intro()
    player_init = player_select()
    com_init = com_select()

    c = init_attack(player_init, com_init, 0)

    case = attack(c[0], c[1], c[2], player_select(), com_select())

    # 게임 진행
    while case[0] == 0 or case[0] == 1:
        case = attack(case[0], case[1], case[2], player_select(), com_select())

    if case[0] == 2:
        print("")
        print("승리!")
        return 0
    elif case[0] == 3:
        print("")
        print("패배...")
        return 1


run()
