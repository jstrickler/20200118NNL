"""
Implement CardDeck class
"""
import random

class CardDeck:
    """
    CardDeck class

    Syntax:
    d = CardDeck("dealer name")
    card = d.draw()
    d.shuffle()

    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        """
        Constructor for CardDeck class

        :param dealer: dealer name as a string
        """
        self.dealer = dealer  # use property
        self._make_deck()

    # def get_dealer(self):  # getter method
    #     return self._dealer

    def _make_deck(self):
        self._cards = []  # cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # make a tuple
                self._cards.append(card)

    @property
    def cards(self):
        """
        List of remaining cards
        :return: List of (rank, suit) tuples
        """
        return self._cards

    def shuffle(self):
        """
        Randomize the current deck

        :return: None
        """
        random.shuffle(self._cards)

    def draw(self):
        """
        Retrieve one card tuple from the deck

        :return: One card as a (rank, suit) tuple
        """
        return self._cards.pop()

    @property
    def dealer(self):  # getter property
        return self._dealer.upper()

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return "{} {}, {}".format(my_name, self.dealer, len(self))






