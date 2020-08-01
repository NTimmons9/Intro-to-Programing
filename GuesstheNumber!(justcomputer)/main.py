print("This is a game where the computer tries to guess your number\nyou will enter a number 1 to 100\nthe computer will try to guess it\nif the computer guessed too high say lower\nif the computer guessed too low say higher\nif the computer got it right say correct")
guessed = False
guess = 0
counter = 0
enterednum = False
stage1 = False
stage2 = True
while enterednum == False:
    num1 = input("Enter a number between 1 and 100: ")
    if num1.isdigit():
        enterednum = True
        num1 = int(num1)
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