import random

def deal_card():
    """Returns a random card from a deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card

def calculate_score(cards):
    """calculate total number of a deck of card list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack :O" 
    elif user_score == 0:
        return "Win with a lucky Blackjack B)"
    elif user_score > 21:
        return "You surpassed 21, You lose"
    elif computer_score > 21:
        return "Opponent surpassed 21, You Win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def blackjackgame():
    user_cards = []
    computer_cards = []
    is_game_over = False

    from blackjacklogo import logo
    print(logo)

    for _ in range(2): #ini ga masuk while loop soalnya dia nambah 2 pas awal doang buat starting
        # new_card = deal_card()
        # user_cards.append(new_card) 
        # user_cards += new_card ini gabisa karena new_card bukan suatu list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your Cards: {user_cards}, current score: {user_score}")
        print(f" Computer's First Card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's strategy
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, your final score was {user_score}")
    print(f"   Computer's final hand: {computer_cards}, your final score was {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n") == "y":
    blackjackgame()


    




     
        






    
    
