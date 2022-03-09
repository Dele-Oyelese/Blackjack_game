import deck_shuffler

deck =deck_shuffler.get_shuffled_deck(deck_shuffler.get_deck())
cards =[]
values =[]
for k, v in deck.items():
    cards.append(k)

print(cards[1])
   
