import random

winner = 0 
round = 1

while round < 8:
        player_one_cards = [10,6,8,9,7,12,7]
        player_two_cards = [7,6,9,5,2,8,11]
        card_player1 = (random.choice(player_one_cards))
        card_player2 = (random.choice(player_two_cards))
        player1_win = 0
        player2_win = 0

        print("Round" + " " + str(round) + " " + ":")
        if card_player1 > card_player2: 
                player1_win =+ 1
                print (" Player 1 wins the round! ", "with", card_player1, "beating", card_player2) 
        elif card_player2 > card_player1: 
                player2_win =+ 1
                print (" Player 2 wins the round! ", "with", card_player2, "beating", card_player1)
        else:
                card_player1 == card_player2
                print("tie")

        round += 1

player1_win, player2_win

if player1_win> player2_win:
        print ( "Player 1 wins the game by", player1_win, "to", player2_win) 
if player2_win> player1_win:
        print ( "Player 2 wins the game by", player2_win, "to", player1_win) 
else : ("tie")               
        
