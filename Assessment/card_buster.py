def play_game():
    ''' This function play all of the game rounds, printing out the winner of each round'''

    global player1_score
    global player2_score 

    player1_cards = [10, 6, 8, 9, 7, 12, 7]
    player2_cards = [7, 6, 9, 5, 2, 8, 11]

    player1_score = 0
    player2_score = 0

    for round_num in range(7):
        player1_card = player1_cards[round_num] #round numbers of round
        player2_card = player2_cards[round_num] #round numbers of round

        if player1_card > player2_card:
            player1_score += 1
            print(f"Player 1 wins round {round_num+1} with card value {player1_card}!") 
        elif player1_card < player2_card:
            player2_score += 1
            print(f"Player 2 wins round {round_num+1} with card value {player2_card}!")
        else:
            print(f"Round {round_num+1} is a tie!")

def final_result():
    """ This function lets the game players know who won the overall game"""
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player1_score < player2_score:
        print("Player 2 wins the game!")
    else:
        print("The game ends in a tie!")

def future_enhacements():
    """ NOthing to see """
    pass

play_game()
final_result()

