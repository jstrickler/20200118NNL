from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Amelia")
print(d1)

print(d1.dealer)  # print 'property'

d1.dealer = 'Balthazar'

print(d1.dealer)

for name in "Bob", 123, None, "Clara":
    try:
        d = CardDeck(name)
    except TypeError as err:
        print(err)
    else:
        print(d.dealer)

d1.shuffle()
print(d1.cards, '\n')

hand = []
for i in range(5):
    hand.append(d1.draw())
print(hand)

print(len(d1.cards))  # SORTA BAD
print(len(d1._cards)) # VERY BAD
print(len(d1))   # GOOD

print(str(d1))

j1 = JokerDeck("Albert")
print(j1)
j1.shuffle()
for i in range(10):
    print(j1.draw())
print()

print(j1.cards)




