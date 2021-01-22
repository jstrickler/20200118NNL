from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call from parent class
        for joker_number in 1, 2:
            joker = (joker_number, 'Joker')
            self._cards.append(joker)
