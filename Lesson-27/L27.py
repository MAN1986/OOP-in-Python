import random
class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __repr__(self):
        return f'{self.value}-{self.suit}'

class Deck:
    def __init__(self):
        self.cards=[]
        for s in ['Spade','Club','Diamond','Heart']:
            for v in ['A','2','3','4','5','6','7',
            '8','9','10','J','Q','K']:
                self.cards.append(Card(s,v))
    def shuffle(self):
        random.shuffle(self.cards)
    def __repr__(self):
        return repr(self.cards)

d=Deck()
d.shuffle()
print(d)
