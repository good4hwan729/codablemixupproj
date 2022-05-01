import card
import random

deck = {'Spade': ['2','3','4','5','6','7','8','9','10'],
        'Clover': ['2','3','4','5','6','7','8','9','10'],
        'Heart': ['2','3','4','5','6','7','8','9','10'],
        'Diamond': ['2','3','4','5','6','7','8','9','10']}
discard_pile = {'Spade': [], 'Clover': [], 'Heart': [], 'Diamond': []}

playing = True

while(playing):
    player_cards, ai_cards = card.game_setup(deck, discard_pile)

    print("Your cards are ", player_cards)
    user_selection = input("Which card would you like to use, 1 or 2?: ")
    user_play = player_cards[int(user_selection)-1]
    ai_play = ai_cards[random.randint(0,1)]

    results = card.check_winner(user_play, ai_play)
    print("Your opponent's card was ", ai_play)

    if results == 1:
        print("You win!")
        playing = False
    elif results == 2:
        print("You lose")
        playing = False
    elif results == 3:
        print("PLay again")


