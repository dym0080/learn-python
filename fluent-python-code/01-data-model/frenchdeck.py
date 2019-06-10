import collections
from random import choice

Card=collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades clubs hearts diamonds'.split()

    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]


beer_card=Card('7','clubs')
print(beer_card)

deck=FrenchDeck()

print(choice(deck))

print(deck[0])