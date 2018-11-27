print("GPA Calculator\n")

numOfClasses = int(input("Enter your number of classes: "))

if numOfClasses == 4:
    grade = float(input("\nEnter the percentage of your first class: "))
    grade1 = float(input("Enter the percentage of your second class: "))
    grade2 = float(input("Enter the percentage of your third class: "))
    grade3 = float(input("Enter the percentage of your fourth class: "))

    totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3)

    GPA = float(totalGrade) / 4

    print("\nYour GPA is: " + str(GPA))

if numOfClasses == 6:
    grade = float(input("\nEnter the percentage of your first class: "))
    grade1 = float(input("Enter the percentage of your second class: "))
    grade2 = float(input("Enter the percentage of your third class: "))
    grade3 = float(input("Enter the percentage of your fourth class: "))
    grade4 = float(input("Enter the percentage of your fifth class: "))
    grade5 = float(input("Enter the percentage of your sixth class: "))

    totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3) + float(grade4) + float(grade5)

    GPA = float(totalGrade) / 6

    print("\nYour GPA is: " + str(GPA))
