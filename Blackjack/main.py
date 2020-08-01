import random
import inspect, re
import sys

global bot
global player
global botTotal
global running
global imrunningoutofideasforvariables
global answerthequestion
global botShow
global reloop

playerTotal = 0
botTotal = 0
wins = 0
running = True
imrunningoutofideasforvariables = True
answerthequestion = True
wins = 0
rounds = 0
botShow = True
reloop = True
blackjackman = False

"""
A = 11
J = 10
Q = 10
K = 10
"""
A = 11

cards = [A,2,3,4,5,6,7,8,9,10,"J","Q","K"]
player = []
bot = []

def randomCards():
    ran1 = random.randint(0,12)
    player.append(cards[ran1])
    ran2 = random.randint(0,12)
    player.append(cards[ran2])
    ran3 = random.randint(0,12)
    bot.append(cards[ran3])
    ran4 = random.randint(0,12)
    bot.append(cards[ran4])
    #print (player)
    #print (bot)

def hit():
    ran1 = random.randint(0,12)
    player.append(cards[ran1])

def bust():
    global playerTotal
    playerTotal = 0
    for i in range(len(player)):
        if player[i] == "J" or player[i] == "Q" or player[i] == "K":
            playerTotal = 10 + playerTotal
        else:
            playerTotal = int(player[i]) + playerTotal
    #print (playerTotal)
    if playerTotal >= 22:
            for i in range(len(player)):
                if player[i] == 11:
                    player[i] = 1
                    #print (player)
                    playerTotal = 0
                    for i in range(len(player)):
                        if player[i] == "J" or player[i] == "Q" or player[i] == "K":
                            playerTotal = 10 + playerTotal
                        else:
                            playerTotal = int(player[i]) + playerTotal
                    #print (playerTotal)
                    break
    #if playerTotal >= 22:
        #gameEnd()
        #print ("You busted!")
        #print ("The dealer Wins\tScore: " + wins + "/" + rounds)

def botHit():
    global botTotal
    botTotal = 0
    for i in range(len(bot)):
        if bot[i] == "J" or bot[i] == "Q" or bot[i] == "K":
            botTotal = 10 + botTotal
        else:
            botTotal = int(bot[i]) + botTotal
    #print (botTotal)
    if botTotal < 17:
        ran3 = random.randint(0,12)
        bot.append(cards[ran3])
        #print (bot)
        botHit()
    botBust()
 
def botBust():
    if botTotal >= 22:
        for i in range(len(bot)):
            if bot[i] == 11:
                bot[i] = 1
                #print (bot)
                botHit()
  
def blackjack():
    if player == [A,10] or player == [10,A] or player == [A,"J"] or player == ["J",A] or player == [A,"Q"] or player == ["Q",A] or player == [A,"K"] or player == ["K",A]:
        print ("blackjack")
        if bot == [A,10] or bot == [10,A] or bot == [A,"J"] or bot == ["J",A] or bot == [A,"Q"] or bot == ["Q",A] or bot == [A,"K"] or bot == ["K",A]:
            print ("stand-off")
            gameEnd()
        else:
            global blackjackman
            blackjackman = True
            gameEnd()

def showCards():
    playerCards = "["
    for j in range(len(player)):
        placeholder = player[j]
        if player[j] == 11 or player[j] == 1:
            placeholder = "A"
        playerCards = playerCards + str(placeholder) + " "
    playerCards = playerCards.strip() + "]"
    botCards = "["
    if botShow == True:
        for i in range(1):
            botplaceholder = bot[i]
            if bot[i] == 11 or bot[i] == 1:
                botplaceholder = "A"
            botCards = botCards + str(botplaceholder) + " "
        botCards = botCards.strip() + " |*|]"
    if botShow == False:
        for i in range(len(bot)):
            botplaceholder = bot[i]
            if bot[i] == 11 or bot[i] == 1:
                botplaceholder = "A"
            botCards = botCards + str(botplaceholder) + " "
        botCards = botCards.strip() + "]"
    print("")
    print("Dealer cards")
    print (botCards)
    botHit()
    botBust()
    if botShow == False:
        print ("Total: " + str(botTotal))
    #print ("Total: " + str(botTotal))
    print("")
    print("")
    print("Your cards")
    print (playerCards)
    bust()
    print ("Total: " + str(playerTotal))

def gameEnd():
    global bot
    global player
    global playerTotal
    global botTotal
    global running
    global imrunningoutofideasforvariables
    global answerthequestion
    global reloop
    global botShow
    botShow = not botShow
    showCards()
    if playerTotal <= 21:
        if playerTotal > botTotal or botTotal > 21 or blackjackman == True:
            global wins
            global rounds
            wins = wins + 1
            print ("You Win\tScore: " + str(wins) + "/" + str(rounds))
        elif playerTotal < botTotal:
            print ("The dealer Wins\tScore: " + str(wins) + "/" + str(rounds))
        elif playerTotal == botTotal:
            print("Stand-off")
            print ("No one Wins\tScore: " + str(wins) + "/" + str(rounds))
    elif playerTotal > 21:
        print("You Busted!")
        print ("The dealer Wins\tScore: " + str(wins) + "/" + str(rounds))
    while reloop:
        rematch = input("Do you want to play again? Y/N: ")
        if rematch.lower() == "y":
            running = False
            bot = []
            player = []
            playerTotal = 0
            botTotal = 0
            running = True
            imrunningoutofideasforvariables = True
            answerthequestion = True
            botShow = True
            reloop = True
            print("<-------------------------------------------------------------->")
            game()
        elif rematch.lower() == "n":
            sys.exit("Good Bye")
    
def game():
    global rounds
    rounds = rounds + 1
    randomCards()
    showCards()
    while running:
        bust()
        botHit()
        botBust()
        blackjack()
        global answerthequestion
        answerthequestion = True
        while answerthequestion:
            if playerTotal < 22:
                SorH = input("Do you want to Stand or Hit: ")
                if SorH.lower() == "stand":
                    answerthequestion = False
                    gameEnd()
                elif SorH.lower() == "hit":
                    hit()
                    showCards()
                    answerthequestion = False
            if playerTotal >= 22:
                SorH = input("You Busted you need to stand: ")
                if SorH.lower() == "stand":
                    answerthequestion = False
                    gameEnd()

        
print ("Welcome to Blackjack")
print ("You will be playing against the dealer which is a bot")
while imrunningoutofideasforvariables:
    rules = input("Do you know how to play blackjack? Y/N: ")
    if rules.lower() == "y":
        print ("Oh okay but just so you know A's will be counted as 11 \nunless that would force a bust then it is counted as a 1")
        imrunningoutofideasforvariables = False
    elif rules.lower() == "n":
        print ("The goal of blackjack is to beat the dealer's hand without going over 21.\nFace cards are worth 10. Aces are worth 1 or 11.\nEach player starts with two cards, one of the dealer's cards is hidden until the end.\nTo 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\nIf you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\nIf you are dealt 21 from the start (Ace & 10), you got a blackjack.")
        print ("Oh and also for this game A's will be counted as 11 \nunless that would force a bust then it is counted as a 1")

        imrunningoutofideasforvariables = False
    
game()