import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(clubs=0, diamonds=1, hearts=2, spades=3)

def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':

    deck = Deck()
    for card in sorted(deck, key=spades_high):
        print(card)
