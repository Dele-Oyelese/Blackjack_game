from dataclasses import replace
import random


def get_deck():
    spades = {'Ace of spades': 11, '2 of spades': 2, '3 of spades': 3, '4 of spades': 4,
                '5 of spades': 5, '6 of spades': 6, '7 of spades':7, '8 of spades': 8, 
                '9 of spades': 9, '10 of spades': 10,'Jack of spades': 10, 
                'Queen of spades': 10, 'King of spades': 10 }


    # create spade keys and values as a list
    spades_keys = list(spades.keys())
    spades_values = list(spades.values())

    # suit name converter 
    diamonds_string_keys =[]
    clubs_string_keys =[]
    hearts_string_keys=[]
    for postions in range(len(spades_keys)):
        hearts_string_keys += [str(spades_keys[postions]).replace('spades', 'hearts')]
        clubs_string_keys += [str(spades_keys[postions]).replace('spades', 'clubs')]
        diamonds_string_keys += [str(spades_keys[postions]).replace('spades', 'diamonds')]

    # suit dictionary creater
    hearts = dict(zip(hearts_string_keys, spades_values))
    diamonds = dict(zip(diamonds_string_keys, spades_values))
    clubs = dict(zip(clubs_string_keys, spades_values))
    # combine deck
    deck = {} 
    for i in (hearts, diamonds, clubs, spades): 
        deck.update(i)
    print(deck)
    return deck


def get_shuffled_deck():
    deck = get_deck()
    #shuffle the deck
    deck_keynames = list(deck.keys())
    #randomize key names
    shuffled_deck_keynames = random.sample(deck_keynames, len(deck_keynames))
    #add random keynames back to values and return shuffled deck
    shuffled_deck_values =[]
    for i in shuffled_deck_keynames:
        shuffled_deck_values += [deck[i]]
    shuffled_deck = dict(zip(shuffled_deck_keynames, shuffled_deck_values))
    return shuffled_deck

get_deck()