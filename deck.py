from random import shuffle


class Card:
    def __init__(self, card_type, number):
        self.card_type = card_type
        self.number = number

    def __str__(self):
        return "type: " + self.card_type + ", number: " + str(self.number)


class Deck:
    def __init__(self, max=40):
        self.max = 40
        self.type_list = ["red", "blue", "green", "yellow"]
        self.number_list = list(range(1,11))
        self.cards = [Card(card_type, number) for card_type in self.type_list for number in self.number_list]

    def __getitem__(self, item):
        return self.cards[item]

    def __bool__(self):
        return len(self.cards) > 0

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)
