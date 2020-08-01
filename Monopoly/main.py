import random

print("Oh No! You got sent to jail. You must roll a double to go free.")

ran1 = 0
ran2 = 1
turn = 0

while ran1 != ran2:
    ran1 = random.randint(1,6)
    ran2 = random.randint(1,6)

    turn = turn + 1
    
    print("Turn " + str(turn) + ": " + str(ran1) + "&" + str(ran2))