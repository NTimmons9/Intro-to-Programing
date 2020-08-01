import random

score = 0
    
def game():
    
    num1 = random.randint(1,3)
    
    global score
    
    player = input("time to play rock papaer scissors please type in your choice: ")
    player = player.lower()
    
    if player == "rock":
        player = 1
    elif player == "scissors":
        player = 2
    elif player == "paper":
        player = 3
    else:
        print("invailid choice")
        game()
    
    if num1 == 1:
        print("the computer picked rock")
        if player == 1:
            print("its a draw! Score: " + str(score))
        elif player == 2:
            print("You lose! Score: " + str(score))
        elif player == 3:
            score = score + 1
            print("you win! Score: " + str(score))
    if num1 == 2:
        print("the computer picked scissors")
        if player == 2:
            print("its a draw! Score: " + str(score))
        elif player == 3:
            print("You lose! Score: " + str(score))
        elif player == 1:
            score = score + 1
            print("you win! Score: " + str(score))
    if num1 == 3:
        print("the computer picked paper")
        if player == 3:
            print("its a draw! Score: " + str(score))
        elif player == 1:
            print("You lose! Score: " + str(score))
        elif player == 2:
            score = score + 1
            print("you win! Score: " + str(score))
            
    replay = input("Play again?")
    replay = replay.lower()
    if replay == "yes":
        game()
    else:
        print("")
        
game()