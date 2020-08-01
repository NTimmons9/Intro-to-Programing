print ("Welcome to the currency exchange")
country = input("Which country would you like to exchange with: ")
amount = input("How much do you want to exchange: ")

giveback = 0

if country.lower() == "china":
    giveback = float(amount) * 7.8

if country.lower() == "england":
    giveback = float(amount) * 0.81
    
if country.lower() == "australia":
    giveback = float(amount) * 1.45




print(round(giveback , 2))