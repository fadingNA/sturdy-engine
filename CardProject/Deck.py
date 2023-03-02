import random

import Cards


class Deck:
    def __init__(self):
        self.all_cards = []  # empty list
        for suit in Cards.suits:
            for rank in Cards.ranks:
                # Create here
                created_card = Cards.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def length(self):
        count = 0
        for i in range(len(self.all_cards)):
            count += 1
        return count


new_deck = Deck()
first_card = new_deck.all_cards[-1]
print(first_card)
for card_object in new_deck.all_cards:
    print(card_object)

new_deck.shuffle()

for i in new_deck.all_cards:
    print(i)

mycard = new_deck.deal_one()
print(mycard)

print(new_deck.length())
