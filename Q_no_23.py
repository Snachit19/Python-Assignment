print("Welcome to the Haunted House")

choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if choice1 == "downstairs":
    print("Game Over")
else:
    if choice1 == "upstairs":
        choice2 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()
        
        if choice2 == "enter the room":
            print("Game Over")
        else:
            if choice2 == "stay outside":
                choice3 = input("Choose between 'ghost', 'vampire', or 'werewolf': ").lower()
                
                if choice3 == "ghost" or choice3 == "vampire":
                    print("Game Over")
                else:
                    if choice3 == "werewolf":
                        print("You Win")
                    else:
                        print("Invalid choice")
            else:
                print("Invalid choice")
    else:
        print("Invalid choice")