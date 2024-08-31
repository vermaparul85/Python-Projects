import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

global playing
playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def __str__(self):
        all_cards_comp = ''
        for card in self.all_cards:
            all_cards_comp += '\n' + card.__str__()

        return 'Deck has: ' + all_cards_comp
        
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_aces(self):
        # if total value is greater than 21 and have ace, change the value of ace to 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips. you have {chips.total} chips ')
            else:
                break

def hit(deck,hand):
    hand.add_cards(deck.deal_one())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing
    
    while True:
        x = input('Hit or Stand? Enter H or S: ').upper()

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands, dealer\'s turn')
            playing = False
        else:
            print('Sorry, please try again!')
            continue
        break

def show_some(player,dealer):
    #show only one card for dealer
    print('\nDealer\'s Hand: ')
    print('First card hidden ')
    print(f'{dealer.cards[1]}')
    
    #show all cards of player
    print('\nPlayer\'s Hand: ')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    #show all cards for dealer, another way to print
    print('\nDealer\'s Hand: ',*dealer.cards,sep='\n')
    print(f'Dealer\'s hand value: {dealer.value}')
    
    #show all cards of player, another way to print
    print('\nPlayer\'s Hand: ',*player.cards,sep='\n')
    print(f'Player\'s hand value: {player.value}')

def player_busts(player,dealer,chips):
    print('BUST Player, Dealer wins!')
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('BUST Dealer, Player wins!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins!')
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH!!')

while True:
    # print an opening statement
    print('Welcome to Blackjack game')

    # create an shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(new_deck.deal_one())
    player_hand.add_cards(new_deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_cards(new_deck.deal_one())
    dealer_hand.add_cards(new_deck.deal_one())
    
    # set up player's chip
    player_chips = Chips()

    # prompt the player for their bet
    take_bet(player_chips)

    # show cards (keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:
        # prompt player to hit ot stand
        hit_or_stand(new_deck, player_hand)

        # show cards (keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # if player's hand exceeds 21, player busts
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # if player has not busted, play dealer's hand until dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(new_deck,dealer_hand)
    
        show_all(player_hand,dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    # inform player of their total chips
    print(f'\nPlayer\'s total chips: {player_chips.total}')
    
    game_on = input('Do you want to play again? Enter Y or N ').upper()

    if game_on[0] == 'Y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break
