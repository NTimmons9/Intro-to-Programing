print ("Welcome to the currency exchange")
country = input("With wich country would you like to exchange China, England, or Australia: ")
amount = input("How much do you want to exchange: ")

giveback = 0

if country.lower() == "china":
    giveback = float(amount) * 7.8
    print ("You get " + str(round(giveback , 2)) + " Chinese renminbi")

if country.lower() == "england":
    giveback = float(amount) * 0.81
    print ("You get " + str(round(giveback , 2)) + " English pounds")
    
if country.lower() == "australia":
    giveback = float(amount) * 1.45
    print ("You get " + str(round(giveback , 2)) + " Australian dollars")