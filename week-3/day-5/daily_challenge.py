import random
class Card:
    
    def __init__(self):
        self.suits = ["♥️", "♣️", "♠️", "♦️"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [{'suit': suit, 'value': value} for suit in self.suits for value in self.values]
    
    
crd = Card()
deck_cards = crd.cards

class Deck:
    
    def __init__(self):
        pass
    
    def shuffle(self, deck_cards):
        print(deck_cards)
        count_cards = len(deck_cards)
        if count_cards == 52:
            random.shuffle(deck_cards)
            print(deck_cards)
        else:
            print("you dont have 52 cards")
            
    def deal(self, deck_cards):
        if not deck_cards:
            print("the deck is empty")
        else:
            return deck_cards.pop()

crd2 = Deck()
crd2.shuffle(deck_cards)
for _ in range(52):
    card = crd2.deal(deck_cards)
    print(f"Dealt: {card}")
    print(deck_cards)
crd2.deal(deck_cards)