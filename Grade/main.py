import random

cool = input("This is a grade app we will demonstrate please press ENTER")

ran1 = round(random.uniform(0,100) , 2)

print(ran1)

if 0 <= ran1 <= 59.4:
    print("F for find a new family")
elif 59.5 <= ran1 <= 62.4:
    print("D- for don't come home")
elif 62.5 <= ran1 <= 66.4:
    print("D for don't come home")
elif 66.5 <= ran1 <= 69.4:
    print("D+ for don't come home")
elif 69.5 <= ran1 <= 72.4:
    print("C- for can't have dinner")
elif 72.5 <= ran1 <= 76.4:
    print("C for can't have dinner")
elif 76.5 <= ran1 <= 79.4:
    print("C+ for can't have dinner")
elif 79.5 <= ran1 <= 82.4:
    print("B- for below average")
elif 82.5 <= ran1 <= 86.4:
    print("B for below average")
elif 86.5 <= ran1 <= 89.4:
    print("B+ for below average")
elif 89.5 <= ran1 <= 92.4:
    print("A- for average")
elif 92.5 <= ran1 <= 96.4:
    print("A for average")
elif 96.5 <= ran1 <= 100:
    print("A+ for average")
   
def cycleGrade():
    grade = float(input("What is your number grade? "))
    
    if 0 <= grade <= 59.4:
        print("F for find a new family")
    elif 59.5 <= grade <= 62.4:
        print("D- for don't come home")
    elif 62.5 <= grade <= 66.4:
        print("D for don't come home")
    elif 66.5 <= grade <= 69.4:
        print("D+ for don't come home")
    elif 69.5 <= grade <= 72.4:
        print("C- for can't have dinner")
    elif 72.5 <= grade <= 76.4:
        print("C for can't have dinner")
    elif 76.5 <= grade <= 79.4:
        print("C+ for can't have dinner")
    elif 79.5 <= grade <= 82.4:
        print("B- for below average")
    elif 82.5 <= grade <= 86.4:
        print("B for below average")
    elif 86.5 <= grade <= 89.4:
        print("B+ for below average")
    elif 89.5 <= grade <= 92.4:
        print("A- for average")
    elif 92.5 <= grade <= 96.4:
        print("A for average")
    elif 96.5 <= grade <= 100:
        print("A+ for average")
        
    cycleGrade()
cycleGrade()