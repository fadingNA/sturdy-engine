import Cards
import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_card):
        if type(new_card) is type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def __str__(self):
        return f'Player -> {self.name} has {len(self.all_cards)} cards'


new_player = Player("non")

print(new_player)
