import random
valid = False
guessed = False
guess = "0"
counter = 0
enterednum = False
stage1 = False
stage2 = True
ran1 = random.randint(1,100)
while valid == False:
    gametype = input("Would you like option 1 or 2\n1.The computer guesses your number\n2.You guess the computers number\n")
    if gametype == "1":
        guess = int(guess)
        valid = True
        print("This is a game where the computer tries to guess your number\nyou will enter a number 1 to 100\nthe computer will try to guess it\nif the computer guessed too high say lower\nif the computer guessed too low say higher\nif the computer got it right say correct")
        while enterednum == False:
            num1 = input("Enter a number between 1 and 100: ")
            if num1.isdigit():
                num1 = int(num1)
                if num1 > 0 and num1 < 100:
                    enterednum = True
                else:
                    print("please enter a valid number")
            else:
                print("please enter a number")
            tip = "higher"
        while stage1 == False:
            while tip.lower() == "higher":
                counter = counter + 1
                guess = guess + 10
                print("is it " + str(guess))
                tip = input("higher, lower, or correct: ")
            stage1 = True
            stage2 = False
        while stage2 == False:
            counter = counter + 1
            guess = guess - 5
            print("is it " + str(guess))
            tip = input("higher, lower, or correct: ")
            while tip.lower() == "lower":
                counter = counter + 1
                guess = guess - 1
                print("is it " + str(guess))
                tip = input("higher, lower, or correct: ")
            while tip.lower() == "higher":
                counter = counter + 1
                guess = guess + 1
                print("is it " + str(guess))
                tip = input("higher, lower, or correct: ")
            if tip.lower() == "correct":
                stage2 = True
                guessed = True
                print("The computer guessed your number it took " + str(counter) + " guesses")
    elif gametype == "2":
        valid = True
        print ("I'm thinking of a number between 1 and 100")
        guess = (input("what do you think the number is: "))
        while guessed == False:
            counter = counter + 1
            if guess.isdigit():
                guess = int(guess)
                if guess > ran1:
                    print("lower")
                elif guess < ran1:
                    print ("higher")
                elif guess == ran1:
                    guessed = True
                    print("You guessed the number!")
                    print("It took " + str(counter) + " tries")
            else:
                print("Please input a number ")
            if guessed == False:
                guess = (input("Guess again: "))
    else:
        print("Please enter a valid option")