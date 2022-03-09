from __future__ import absolute_import
from re import S
import time

from aem import con
from dealer import Dealer
from player import Player
import deck_shuffler

class BlackJack():
    def __init__(self, dealer: Dealer, player: Player, deck:dict ={}): 
        self.dealer = dealer
        self.player = player
        self.deck = deck
  
    def deal_cards(self):
        ## dealing cards
        for num_cards in range(2):
            self.dealer.cards.update(self.dealer.get_card(self.deck))
            self.player.cards.update(self.player.get_card(self.deck))

    def dealers_card(self):
        #print only the dealers second card
        dealer_key =[]
        dealer_value =[]
        for k,v in self.dealer.cards.items():
            dealer_key.append(k) 
            dealer_value.append(v)
        print(f"The dealer has a {dealer_key[1]}")
        print(f"for a value of {dealer_value[1]}")
        return dealer_key, dealer_value

    ### def key_compare(self,user_answer):
        valid_answers = ["hit", "stand", "exit"]
        validator = bool
        user_answer =str.lower(user_answer)
        for answers in valid_answers:
            if answers == user_answer:
                validator = True
                break
            else:
                validator = False
        return validator ###
        #print(f"{name}'s cards are {current_hand.keys()} for a total of {sum(current_hand.values())}")

    def ace_counter(self, current_hand: dict ={}):
        # checks for aces and stores the cardname and also prints current hand
        ace_count = 0
        keyset =[]
        for cards, value in current_hand.items():
            if value == 11:
                ace_count += 1
                keyset.append(cards)
        return keyset,ace_count
    
    def current_hand(self, current_hand: dict ={} , name = ""):
        keyset,ace_count = self.ace_counter(current_hand)
        if ace_count >= 1 :
            print(f"{name}'s cards are", ', '.join(current_hand))
            print(f"for a total of {sum(current_hand.values())} or {sum(current_hand.values()) - (10 * ace_count)}")
            print("---------------------------------")
        else: 
            print(f"{name}'s cards are", ', '.join(current_hand))
            print(f"for a total of {sum(current_hand.values())}")
            print("---------------------------------")

    def ace_replace(self,current_hand: dict ={}):
        keyset, ace_count = self.ace_counter(current_hand)
        i = 0 #iterator of ace postion
        while (sum(current_hand.values()) > 21 and ace_count >= 1):
            card =(keyset[i])
            current_hand[card] = 1 
            i+= 1
        print(sum(current_hand.values()))

    def bust_or_not(self,current_hand: dict ={}, name =""):
        bust= bool
        if sum(current_hand.values())<21:
            self.current_hand(current_hand,name)

        if sum(current_hand.values()) > 21:
            self.ace_replace(current_hand)
            if sum(current_hand.values()) > 21:
                print(f"{name}'s cards are ", ', '.join(current_hand), f" for a total of {sum(current_hand.values())}")
                bust = True
                return bust
            else:
                print(f"{name}'s cards are ", ', '.join(current_hand), f" for a total of {sum(current_hand.values())}")
                bust = False
                return bust
    
    def hit_or_stand(self):
        ## create hit or stand
        looper = False
        while looper == False:
            print("---------------------------------")
            hit_stand = input("Would you like to hit or stand? Or type 'exit' if you would like to exit\n")
            hit_stand = str.lower(hit_stand)
            
            #hit condition
            if hit_stand == "hit":
                
                self.player.cards.update(self.player.get_card(self.deck))
                bust = self.bust_or_not(self.player.cards, self.player.name)
                
                if bust == True:
                    self.player.bust = True
                    print("---------------------------------")
                    print("sorry you busted!")
                    break
                else:

                    looper = False
                    continue
                
            
            #other conditions
            elif hit_stand == "stand":
                looper = True
            elif hit_stand == "exit":
                exit()
            else:
                print("You did not enter a valid response please try again.")
                print("---------------------------------")
    def dealer_play(self):
        self.current_hand(self.dealer.cards, self.dealer.name)

        while sum(self.dealer.cards.values())< 16:
            if self.player.bust == True:
                break
            time.sleep(1)
            self.dealer.cards.update(self.dealer.get_card(self.deck))
            bust = self.bust_or_not(self.dealer.cards, self.dealer.name)
            if bust == True:
                self.dealer.bust = True
                print("Dealer busted !!")
    
    def card_compare(self):
        time.sleep(.8)
        if (((sum(self.player.cards.values()) < sum(self.dealer.cards.values())) and self.dealer.bust == False) or self.player.bust == True):
            print("Sorry the dealer won")
        elif (sum(self.player.cards.values()) == sum(self.dealer.cards.values()) and self.player.bust == False):
            print("The dealer pushed")
        elif (sum(self.player.cards.values()) > sum(self.dealer.cards.values()) and self.player.bust == False):
            print("Congrats you Won!")
         
    def continue_play(self):
        yes_no = False
        while yes_no == False:
            print("---------------------------------")
            play = input ("Would you like to play again (Y/N)?\n")
            play = str.lower(play)
            if play == "y":
                yes_no = True
                return yes_no
            elif play == "n":
                exit()
            else:
                print("That wasnt a vaild response please type Y or N")




    def play(self):
        continue_play = True
        while continue_play == True:
            # Initalized shuffled Deck
            self.deck = deck_shuffler.get_shuffled_deck() 
## Need to figure out a way to re-initalize players and Dealers hand 
        
            # dealing cards
            self.deal_cards()

            # print the players card
            self.current_hand(self.player.cards,self.player.name)
            
            # print dealers second card only
            time.sleep(.8)
            self.dealers_card()

            # hit or stand
            self.hit_or_stand()

            # see if the dealer busts
            self.dealer_play()

            self.card_compare()

            continue_play = self.continue_play()

