import random

deck_of_cards = {
    "2♠": 2, "2♥": 2, "2♦": 2, "2♣": 2,
    "3♠": 3, "3♥": 3, "3♦": 3, "3♣": 3,
    "4♠": 4, "4♥": 4, "4♦": 4, "4♣": 4,
    "5♠": 5, "5♥": 5, "5♦": 5, "5♣": 5,
    "6♠": 6, "6♥": 6, "6♦": 6, "6♣": 6,
    "7♠": 7, "7♥": 7, "7♦": 7, "7♣": 7,
    "8♠": 8, "8♥": 8, "8♦": 8, "8♣": 8, 
    "9♠": 9, "9♥": 9, "9♦": 9, "9♣": 9, 
    "10♠": 10,"10♥": 10,"10♦": 10,"10♣": 10,
    "11♠": 10,"11♥": 10,"11♦": 10,"11♣": 10,
    "12♠": 10,"12♥": 10,"12♦": 10,"12♣": 10
    # "A♠": [1, 11], "A♥": [1, 11], "A♦": [1, 11], "A♣": [1, 11] <== add code later to include the use of Aces
    } 

# Global Variables 
player_hand = []  # list for player's cards
dealer_hand = []  # list for dealer's cards
player_total_sum = 0 # player total sum of card amount 
dealer_total_sum = 0 # dealer total sum of card amount 

# Find sum for both player and dealer
def hand_sum():
    global player_total_sum
    player_total_sum = 0
    for k in player_hand:
        player_total_sum += deck_of_cards.get(k)
    return player_total_sum

def dealer_hand_sum():
    global dealer_total_sum
    dealer_total_sum = 0
    for k in dealer_hand:
        dealer_total_sum += deck_of_cards.get(k)
    return dealer_total_sum

cards_to_deal = 0 # cards to be delt to start game

def deal_player_card():
    global cards_to_deal

    if cards_to_deal < 2:
        for card, value in deck_of_cards.items():
            if cards_to_deal != 2:
                player_hand.append(random.choice(list(deck_of_cards.keys())))
                cards_to_deal += 1
    # deals un-delt cards
    elif cards_to_deal == 2:
        unused_card = random.choice(list(deck_of_cards.keys()))

        while unused_card in player_hand or unused_card in dealer_hand:
            unused_card = random.choice(list(deck_of_cards.keys()))
        player_hand.append(unused_card)

deal_player_card()

display_hand = " ".join(player_hand)

print("Your cards: \n" + display_hand)

def deal_dealer_card():
    global display_dealer_hand
    unused_card = random.choice(list(deck_of_cards.keys()))

    while unused_card in player_hand or unused_card in dealer_hand:
        unused_card = random.choice(list(deck_of_cards.keys()))
    dealer_hand.append(unused_card)

    display_dealer_hand = " ".join(dealer_hand)

    if len(dealer_hand) == 2:
        print("Dealer cards: \n" + display_dealer_hand)
    else:
        print("Dealer cards: \n" + display_dealer_hand + " ?")

deal_dealer_card()

next_player_move = "" # variable for determining if while loop continues or ends 

hand_sum()

bust = "false" # if variable is "true" game immediately ends

while next_player_move != "s":
    next_player_move = input("\nType H for hit or S to stand: ") 
    next_player_move.lower()
    if next_player_move == 'h':
        deal_player_card()
        hand_sum()
        display_hand = " ".join(player_hand)
        print("Your cards: \n" + display_hand)
        print("Dealer cards: \n" + display_dealer_hand + " ?")
    if player_total_sum > 21:
        print("Bust, Sorry you lose!")
        bust = "true"
        break


# if bust is false, game decision logic occurs
if bust != "true":
    print("Your cards: \n" + display_hand)

    deal_dealer_card()
    dealer_hand_sum()
    hand_sum()

    if dealer_total_sum > player_total_sum and dealer_total_sum <= 21:
        print("Dealer Winds")
    elif dealer_total_sum < player_total_sum and player_total_sum <= 21:
        print("You Win!")
    elif dealer_total_sum == player_total_sum:
        print("Its a draw!")
