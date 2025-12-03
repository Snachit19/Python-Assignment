p1 = input("Player 1, enter your move (rock, paper, or scissors): ").lower()
p2 = input("Player 2, enter your move (rock, paper, or scissors): ").lower()

# Compare the moves using nested if-else
if p1 == p2:
    print("It's a tie!")

else:
    if p1 == "rock":
        if p2 == "scissors":
            print("Player 1 wins! Rock beats scissors.")
        else:
            print("Player 2 wins! Paper beats rock.")

    else:
        if p1 == "paper":
            if p2 == "rock":
                print("Player 1 wins! Paper beats rock.")
            else:
                print("Player 2 wins! Scissors beat paper.")

        else:
            if p1 == "scissors":
                if p2 == "paper":
                    print("Player 1 wins! Scissors beat paper.")
                else:
                    print("Player 2 wins! Rock beats scissors.")
            else:
                print("Invalid input from Player 1.")