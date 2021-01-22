
def make_deck():
    pass

def deal():
    pass

def shuffle():
    pass

# --- in main ---

d = make_deck()
shuffle(d)
hand = []
for i in range(5):
    hand.append(deal(d))

from carddeck import CardDeck

d = CardDeck("Sam")
print(d.dealer)
d.shuffle()
hand = []
for i in range(5):
    hand.append(d.deal())

print()

