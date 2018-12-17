# This is my Grade Percent Average Calculator Subalgorithm (GPerA)


def gpera():

    # print("\nGrade Percent Average Calculator")

    numOfClasses = int(input("\nEnter your number of classes: \n"))

    if numOfClasses == 4:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))

        totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3)

        GPA = float(totalGrade) / 4

        print("\nYour Grade Percent Average is: " + str(GPA))

    elif numOfClasses == 6:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))
        grade4 = float(input("Enter the percentage of your fifth class: \n"))
        grade5 = float(input("Enter the percentage of your sixth class: \n"))

        totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3) + float(grade4) + float(grade5)

        GPA = float(totalGrade) / 6

        print("\nYour Grade Percent Average is: " + str(GPA))

    else:
        print("\nSorry, this calculator does not support that amount of classes. ")
