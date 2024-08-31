import random
from IPython.display import clear_output
from art import blackjack_logo

def deal_card():
    '''Returns a randon card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    '''Take a lost of cards and returns sum of all cards'''
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)

def compare(dealer_value,player_value):
    '''Compare the player and dealer\'s score'''
    if dealer_value == player_value:
        print('Its a Tie!!!')
    elif dealer_value == 0:
        print('You Lose!!!')
    elif player_value == 0:
        print('You Win!!!')
    elif player_value > 21:
        print('You Lose!!!')
    elif dealer_value > 21:
        print('You Win!!!')
    elif dealer_value < player_value:
        print('You Win!!!')
    elif dealer_value > player_value:
        print('You Lose!!!')

def play_game():
    print(blackjack_logo)
    player_card = []
    dealer_card = []
    is_game_over = False
    
    for _ in range(2):
        player_card.append(deal_card())
        dealer_card.append(deal_card())
    
    while not is_game_over:
        player_value = calculate_score(player_card)
        dealer_value = calculate_score(dealer_card)
        
        print(f'Your Cards: {player_card}, Your Score: {player_value}')
        print(f'Dealer First Card: {dealer_card[0]}')
        
        if player_value == 0 or dealer_value == 0 or player_value > 21:
            is_game_over = True
        else:
            hit_or_stand = input('Do you want another card? Type "Yes" or "No": ').lower()
                
            if hit_or_stand == 'yes':
                player_card.append(deal_card())
            else:
                is_game_over = True
        
    while dealer_value != 0 and dealer_value < 17:
        dealer_card.append(deal_card())
        dealer_value = calculate_score(dealer_card)
    
    print(f'Your final hand: {player_card}, Your final score: {player_value}')
    print(f'Dealer\'s final hand: {dealer_card}, Dealer\'s final score: {dealer_value}')
    compare(dealer_value,player_value)

while(input('Do you want to play Blackjack Game? Type "Yes" or "No": ').lower()) == 'yes':
    clear_output()
    play_game()
