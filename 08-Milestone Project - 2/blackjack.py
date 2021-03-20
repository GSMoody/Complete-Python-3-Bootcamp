# -*- coding: utf-8 -*-
"""
 A Blackjack game written in Python
 
"""
import random

# Variables to define card deck. The value of a card is its rank, except for 
# face cards which have a value of 10, and aces which can have a value of 
# either 1 or 11. 
ace_value = 1
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':ace_value}

##############################################################################
# CLASSES FOR BLACKJACK GAME
##############################################################################
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck():
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def __str__(self):
        return self.all_cards 
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()        
    
class Hand():
    
    def __init__(self, hide_card):
        # A new player has an empty hand
        self.hand= [] 
        self.hide_card = hide_card
        
    def __str__(self):
        cards = ""
        if not self.hide_card:    
            for card in self.hand:
                cards = cards + str(card)
                cards = cards +" ; "
        else:
            for card in self.hand[:-1]:
                cards = cards + str(card)
                cards = cards +" ; "
        return cards
        
    def add_card(self, card):
        self.hand.append(card)
                
    def calculate_hand_value(self):
        value = 0
        if not self.hide_card:
            for card in self.hand:
                if card.rank != 'Ace':
                    value += card.value
                else:
                    value += ace_value
        else:
            for card in self.hand[:-1]:
                if card.rank != 'Ace':
                    value += card.value
                else:
                    value += ace_value
        
        return value
                
class Money():
    def __init__(self):
        self.total = 0
        
    def __str__(self):
        return str(self.total)
        
    def win_bet(self, win):
        self.total += win
    
    def lose_bet(self, loss):
        self.total -= loss
        
##############################################################################
# FUNCTIONS FOR BLACKJACK GAME
##############################################################################

# Function to take the value of the player bet
def take_bet():
    try: 
        bet = int(input("Enter value to bet:"))
        return bet
    except:
        "Exception! Please enter an integer value."
     
# Function to 'hit' a card (deal a card from the deck and add to a hand)
def hit(deck, hand):
    hand.add_card(deck.deal())

# Function to determine if player wants to hit (see above) or stand (pass)
def hit_or_stand():
    while True:
        player_dec = input("Please enter (h/H) to hit or (s/S) to stand.")
        if player_dec in ['h', 'H']:
            hit(deck, player_hand)
        elif player_dec in ['s', 'S']:
            # If player stands the dealer will play. The dealer will always hit 
            # until their hand has a value >= 17
            while dealer_hand.calculate_hand_value() < 17:
                hit(deck, dealer_hand)
            break
        else:
            print("Error! Please enter a valid input (h/H) or (s/S).")

# Function to show cards. Full player hand and value is always shown. 
# If endgame is not reached, one dealer card is hidden and rest are shown along
# with their value. 
# If the endgame is reached, full dealer hand and value is shown. 
def show_cards():
    print("PLAYER HAND:")
    print(player_hand)
    player_value = player_hand.calculate_hand_value()
    print(f"Value of Player Hand: {str(player_value)}\n")
    print("DEALER HAND:")
    print(dealer_hand)      
    dealer_value = dealer_hand.calculate_hand_value()
    print(f"Value of Dealer Hand: {str(dealer_value)}\n")


# Function to determine if any of four possible endgame scenarios have been 
# met: either a Player win/bust or a Dealer win/bust
def is_endgame(bet_amount):
    player_value = player_hand.calculate_hand_value()
    dealer_value = dealer_hand.calculate_hand_value()
    if player_value > 21:
        print("\nPLAYER BUSTS!\n")
        player_money.lose_bet(bet_amount)
        print(f"Player money is £{player_money}.00")
        dealer_hand.hide_card = False 
        return True
    if dealer_value > 21:
        print("\nDEALER BUSTS!\n")
        player_money.win_bet(bet_amount)
        print(f"Player money is £{player_money}.00")
        dealer_hand.hide_card = False 
        return True
    # We know at this point that both player and dealer value are <= 21
    if player_value > dealer_value:
        print("\nPLAYER WINS!\n")
        player_money.win_bet(bet_amount)
        print(f"Player money is £{player_money}.00")
        dealer_hand.hide_card = False 
        return True        
    elif player_value < dealer_value:
        print("\nDEALER WINS!\n")
        player_money.lose_bet(bet_amount)
        print(f"Player money is £{player_money}.00")
        dealer_hand.hide_card = False 
        return True
    else: # Tie 
        print("Push! Player and Dealer Tie.")
        dealer_hand.hide_card = False 
        return True
    
    return False



##############################################################################
# MAIN GAME
##############################################################################

# Initialize player money as £0.00
player_money = Money()
    
while True:
    #Initialize empty deck and shuffle 
    deck = Deck()
    deck.shuffle()
    # Player and dealer both start with empty hands. One dealer card will 
    # always be hidden to the player. 
    player_hand = Hand(hide_card=False)
    dealer_hand = Hand(hide_card=True)
    # Player and dealer hit two cards each in beginning of game
    hit(deck, dealer_hand)
    hit(deck, dealer_hand)
    hit(deck, player_hand)
    hit(deck, player_hand)
    
    while True:
    # Determine the value of the bet amount
        try:
            bet_amount = int(input("Enter value for bet"))
            break
        except:
            print("Error! Please enter an integer value.")
    print(f"\nValue of bet is £{bet_amount}.00\n")
    
    # while loop to play the game until one of the endgame conditions is met
    endgame  = False
    while not endgame:
        # Show the cards at beginning of round
        show_cards()
        # Give the player the option to adjust the value of an ace, it can 
        # either be 1 or 11. 
        adjust_ace_value = input(f"Ace value is currently {ace_value}. Do you want to adjust ace value and recalculate? Enter (y/Y) to readjust")
        if adjust_ace_value in ['y', 'Y']:
            if ace_value == 1:
                ace_value = 11
            else:
                ace_value = 1
            # Show the cards again if ace value is adjusted. 
            show_cards()
        hit_or_stand()
        
        # Determine is endgame scenario is reached
        endgame = is_endgame(bet_amount)
    
    # Game is over now, show the cards one more time. Give player option to 
    # replay.
    show_cards()
    if input("Play again? Enter (y/Y)") not in ['y','Y']:
        break
