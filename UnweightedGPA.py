# This is my Unweighted GPA Calculator Subalgorithm (UGPA)


def ugpa():

    # print("\nUnweighted GPA Calculator\n")

    numOfClasses = int(input("\nEnter your number of classes: \n"))

    if numOfClasses == 4:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))

        if grade >= 90 and grade <= 100:
            gradePt = 4
        elif grade >= 80 and grade <= 89.9:
            gradePt = 3
        elif grade >= 70 and grade <= 79.9:
            gradePt = 2
        elif grade >= 60 and grade <= 69.9:
            gradePt = 1
        else:
            gradePt = 0

        if grade1 >= 90 and grade1 <= 100:
            gradePt1 = 4
        elif grade1 >= 80 and grade1 <= 89.9:
            gradePt1 = 3
        elif grade1 >= 70 and grade1 <= 79.9:
            gradePt1 = 2
        elif grade1 >= 60 and grade1 <= 69.9:
            gradePt1 = 1
        else:
            gradePt1 = 0

        if grade2 >= 90 and grade2 <= 100:
            gradePt2 = 4
        elif grade2 >= 80 and grade2 <= 89.9:
            gradePt2 = 3
        elif grade2 >= 70 and grade2 <= 79.9:
            gradePt2 = 2
        elif grade2 >= 60 and grade2 <= 69.9:
            gradePt2 = 1
        else:
            gradePt2 = 0

        if grade3 >= 90 and grade3 <= 100:
            gradePt3 = 4
        elif grade3 >= 80 and grade3 <= 89.9:
            gradePt3 = 3
        elif grade3 >= 70 and grade3 <= 79.9:
            gradePt3 = 2
        elif grade3 >= 60 and grade3 <= 69.9:
            gradePt3 = 1
        else:
            gradePt3 = 0

        totalPtGrade = int(gradePt) + int(gradePt1) + int(gradePt2) + int(gradePt3)

        GPA = totalPtGrade / 4

        print("\nYour GPA is: " + str(GPA))

    elif numOfClasses == 6:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))
        grade4 = float(input("Enter the percentage of your fifth class: \n"))
        grade5 = float(input("Enter the percentage of your sixth class: \n"))

        if grade >= 90 and grade <= 100:
            gradePt = 4
        elif grade >= 80 and grade <= 89.9:
            gradePt = 3
        elif grade >= 70 and grade <= 79.9:
            gradePt = 2
        elif grade >= 60 and grade <= 69.9:
            gradePt = 1
        else:
            gradePt = 0

        if grade1 >= 90 and grade1 <= 100:
            gradePt1: int = 4
        elif grade1 >= 80 and grade1 <= 89.9:
            gradePt1: int = 3
        elif grade1 >= 70 and grade1 <= 79.9:
            gradePt1: int = 2
        elif grade1 >= 60 and grade1 <= 69.9:
            gradePt1: int = 1
        else:
            gradePt1 = 0

        if grade2 >= 90 and grade2 <= 100:
            gradePt2: int = 4
        elif grade2 >= 80 and grade2 <= 89.9:
            gradePt2: int = 3
        elif grade2 >= 70 and grade2 <= 79.9:
            gradePt2: int = 2
        elif grade2 >= 60 and grade2 <= 69.9:
            gradePt2: int = 1
        else:
            gradePt2 = 0

        if grade3 >= 90 and grade3 <= 100:
            gradePt3: int = 4
        elif grade3 >= 80 and grade3 <= 89.9:
            gradePt3: int = 3
        elif grade3 >= 70 and grade3 <= 79.9:
            gradePt3: int = 2
        elif grade3 >= 60 and grade3 <= 69.9:
            gradePt3: int = 1
        else:
            gradePt3 = 0

        if grade4 >= 90 and grade4 <= 100:
            gradePt4: int = 4
        elif grade4 >= 80 and grade4 <= 89.9:
            gradePt4: int = 3
        elif grade4 >= 70 and grade4 <= 79.9:
            gradePt4: int = 2
        elif grade4 >= 60 and grade4 <= 69.9:
            gradePt4: int = 1
        else:
            gradePt4 = 0

        if grade5 >= 90 and grade5 <= 100:
            gradePt5: int = 4
        elif grade5 >= 80 and grade5 <= 89.9:
            gradePt5: int = 3
        elif grade5 >= 70 and grade5 <= 79.9:
            gradePt5: int = 2
        elif grade5 >= 60 and grade5 <= 69.9:
            gradePt5: int = 1
        else:
            gradePt5 = 0

        totalPtGrade = int(gradePt) + int(gradePt1) + int(gradePt2) + int(gradePt3) + int(gradePt4) + int(gradePt5)

        GPA = totalPtGrade / 6

        print("\nYour GPA is: " + str(GPA))

    else:
        print("\nSorry, this calculator does not support that amount of classes.")

