
player1_cards = [10, 6, 8, 9, 7, 12, 7]
player2_cards = [7, 6, 9, 5, 2, 8, 11]

player1_score = 0
player2_score = 0

for round_num in range(7):
    player1_card = player1_cards[round_num]
    player2_card = player2_cards[round_num]

    if player1_card > player2_card:
        player1_score += 1
        print(f"Player 1 wins round {round_num+1} with card value {player1_card}!")
    elif player1_card < player2_card:
        player2_score += 1
        print(f"Player 2 wins round {round_num+1} with card value {player2_card}!")
    else:
        print(f"Round {round_num+1} is a tie!")

if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player1_score < player2_score:
    print("Player 2 wins the game!")
else:
    print("The game ends in a tie!")