username = input("What do you want your username to be: ")

password = input("What do you want your password to be: ")

attempts = 0

def login():
    
    global attempts
    
    username1 = input("What is your username: ")
    
    password1 = input("What is your passowrd: ")
    
    attempts = attempts + 1
    
    if username1 == username and password1 == password1:
        print("you have logged in")
        
    if username1 == username and password1 != password1:
        print("Your username or password is inncorect")
        if attempts < 3:
            login()
        elif attempts >= 3:
            print("You are out of attempts")
            
    if username1 != username and password1 == password1:
        print("Your username or password is inncorect")
        if attempts < 3:
            login()
        elif attempts >= 3:
            print("You are out of attempts")
            
login()