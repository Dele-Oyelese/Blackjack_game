
class Dealer():
    def __init__(self, name, cards :dict = {},bust = False):
        self.name = name
        self.cards = cards
        self.bust = bust
    def get_card(self,deck: dict, card={}):
        k, v = deck.popitem()
        card[k] = v
        return card
  