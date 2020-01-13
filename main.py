from deck import Deck
if __name__ == "__main__":
    my_deck = Deck()
    for card in my_deck:
        print(card)
    my_deck.shuffle()
    while True:
        if my_deck:
            card = my_deck.deal()
            print(card)
        else:
            print("deck is empty")
            break
