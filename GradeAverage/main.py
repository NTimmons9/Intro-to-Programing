studentnum = int(input("How many students are in the class?"))
grades = []
average = 0
    
for i in range(studentnum):
    grade1 = int(input("Enter a grade: "))
    grades.append(grade1)

for i in range(studentnum):
    average = average + grades[studentnum - (i + 1)]
print("The average is " + str(average/studentnum))