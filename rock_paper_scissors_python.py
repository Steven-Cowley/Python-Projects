# simulation of rock papaer scissors
import random

# initalize playable objects
playable = ["rock", "paper", "scissors"]

running = True

while running:
    # prompt user for their choice
    userPlayed = input('''Enter "rock" "paper" or "scissors": ''')
    # check if user has entered a correct object
    if userPlayed in "rock" or "paper" or "scissors":
        # choose a random element from the playable list
        aiPlayed = random.choice(playable)
        # use a match statement to match the user input to the possibilites and simulate main game
        match userPlayed:
            # if user plays rock
            case "rock":
                # check ai draw
                if aiPlayed == "paper":
                    # print result
                    print(f"AI chooses: {aiPlayed} AI wins")
                elif aiPlayed == "scissors":
                    print(f"AI chooses: {aiPlayed} you win!")
                else:
                    print(f"AI chooses: {aiPlayed} it's a tie")
            case "paper":
                if aiPlayed == "rock":
                    print(f"AI chooses: {aiPlayed} you win!")
                elif aiPlayed == "scissors":
                    print(f"AI chooses: {aiPlayed} AI wins")
                else:
                    print(f"AI chooses: {aiPlayed} it's a tie")
            case "scissors":
                if aiPlayed == "rock":
                    print(f"AI chooses: {aiPlayed} AI wins")
                elif aiPlayed == "paper":
                    print(f"AI chooses: {aiPlayed} you win!")
                else:
                    print(f"AI chooses: {aiPlayed} it's a tie")
    # if user enteres anything other than rock, paper or scissors: break the loop and prompt again
    else:
        break
        
