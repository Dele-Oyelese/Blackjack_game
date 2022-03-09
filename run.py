import game
import player
import dealer

def run():
    dealer1 = dealer.Dealer("dealer")
    player1 = player.Player("Dele")

    game1 = game.BlackJack(dealer1, player1)
    game1.play()

if __name__ == '__main__':
    run()