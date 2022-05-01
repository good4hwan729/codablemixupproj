import numpy as np
import random


#Spade > Clover > Heart > Diamond > Spade
#Numbers

def game_setup(deck, discard_pile):
    player = []
    ai = []

    for _ in range(2):
        player.append(get_card(deck, discard_pile))
        ai.append(get_card(deck, discard_pile))

    return player, ai

def get_card(deck, discard_pile):
    card_suite = random.choice(list(deck)) 
    card_num = deck[card_suite][random.randint(0, len(deck[card_suite]))]
    
    discard_pile[card_suite] += card_num
    deck[card_suite].remove(card_num)

    return (card_suite, card_num)

def check_winner(p1, p2):
    p1_suite = p1[0]
    p2_suite = p2[0]

    if (p1_suite == 'Spade' and p2_suite == 'Clover') or (p1_suite == 'Clover' and p2_suite == 'Heart') or (p1_suite == 'Heart' and p2_suite == 'Diamond') or (p1_suite == 'Diamond' and p2_suite == 'Spade'):
        return 1
    elif (p1_suite == 'Clover' and p2_suite == 'Spade') or (p1_suite == 'Heart' and p2_suite == 'Clover') or (p1_suite == 'Diamond' and p2_suite == 'Heart') or (p1_suite == 'Spade' and p2_suite == 'Diamond'):
        return 2
    elif p1[1] > p2[1]:
        return 1
    elif p1[1] < p2[1]:
        return 2
    else:
        return 3

# print(game_setup(deck, discard_pile))


