import numpy as np
import time
import random
import os

def print_board(player_board):
    print()
    c = int(len(player_board) / 3)
    for i in range(3):
        print(player_board[i*col:i*col+col])
    print()

def get_index(x, y, col):
    return x*col + y

def get_row():
    v = str(input("Select row number (1-3): "))
    while not v.isdigit() or int(v) > 3 or int(v) < 1:
        print("Invalid response. Integer between 1 and 3 only please.")
        v = str(input("Select row number (1-3): "))
    return int(v)

def get_col(col):
    v = str(input("Select column number (1-"+ str(col) +"): "))
    while not v.isdigit() or int(v) > col or int(v) < 1:
        print("Invalid response. Integer between 1 and "+ str(col) +" only please.")
        v = str(input("1: Select column number (1-"+ str(col) +"): "))
    return int(v)

# 6 pairs = 12 (3,4), 9 pairs = 18 (3,6), 12 pairs = 24
num_pairs = 6

l = [i+1 for i in range(0, num_pairs)] + [i+1 for i in range(0, num_pairs)]
random.shuffle(l)
row, col = 3, int(2 * num_pairs / 3)
board = np.array(l).reshape(row, col)
answer = set()
removed = set()

for i in range(0, num_pairs):
    k = [val for val, e in enumerate(l) if e == i+1]
    answer.add((k[0], k[1]))

player_board = ["O"] * row * col

# print(board)
print_board(l)
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

while (len(answer) != 0):
    print_board(player_board)
    print("Choose your first card")
    x1 = get_row()
    y1 = get_col(col)
    i1 = (x1-1)*col + (y1-1)

    while i1 in removed:
        print("You picked removed card. Please select a valid card")
        x1 = get_row()
        y1 = get_col(col)
        i1 = (x1-1)*col + (y1-1)

    player_board[i1] = str(l[i1])
    print_board(player_board)

    print("Choose your second card")
    x2 = get_row()
    y2 = get_col(col)
    while (x1 == x2 and y1 == y2):
        print("Duplicate selection! Try again")
        x2 = get_row()
        y2 = get_col(col)
    i2 = (x2-1)*col + (y2-1)

    while i2 in removed:
        print("You picked removed card. Please select a valid card")
        x2 = get_row()
        y2 = get_col(col)
        i2 = (x2-1)*col + (y2-1)

    player_board[i2] = str(l[i2])
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(player_board)
    time.sleep(1)

    if i1 < i2:
        key = (i1, i2)
    else:
        key = (i2, i1)

    if key in answer:
        removed.add(i1)
        removed.add(i2)
        answer.remove(key)
        player_board[i1] = "X"
        player_board[i2] = "X"
        print("Great work!")
    else:
        player_board[i1] = "O"
        player_board[i2] = "O"
        print("Wrong answer! You have selected " + str(l[i1]) + " and " + str(l[i2]) + ". Try again")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
