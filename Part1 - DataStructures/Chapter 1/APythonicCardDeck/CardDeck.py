import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __str__(self):
        return f'Card({self.ranks}, {self.suits})'
    

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()

print('A deck responds to the len() function by returning the number of cards in it -->' + str(len(deck)))
print('Reading specific cards from the deck—say, the first or the last—is easy, thanks to the __getitem__ method -->' + str(deck[0]))

i=0
while i < 5:
    random_card = choice(deck)
    print(random_card)
    i = i+1

top_3_deck = deck[:3]

for card in deck:
    print(card)

print(Card('A', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)