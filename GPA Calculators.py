print("GPA Calculators")

chooseCalc = input("\nWould you like to calculate your Grade Percent Average, \nUnweighted Grade Point Average, "
                   "or your Weighted Grade Point Average? \n")

if chooseCalc == "Grade Percent Average" or "grade percent average" or "GRADE PERCENT AVERAGE":

    numOfClasses = int(input("\nEnter your number of classes: \n"))

    if numOfClasses == 4:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))

        totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3)

        GPA = float(totalGrade) / 4

        print("\nYour GPA is: " + str(GPA))

    elif numOfClasses == 6:

        grade = float(input("\nEnter the percentage of your first class: \n"))
        grade1 = float(input("Enter the percentage of your second class: \n"))
        grade2 = float(input("Enter the percentage of your third class: \n"))
        grade3 = float(input("Enter the percentage of your fourth class: \n"))
        grade4 = float(input("Enter the percentage of your fifth class: \n"))
        grade5 = float(input("Enter the percentage of your sixth class: \n"))

        totalGrade = float(grade) + float(grade1) + float(grade2) + float(grade3) + float(grade4) + float(grade5)

        GPA = float(totalGrade) / 6

        print("\nYour GPA is: " + str(GPA))

    else:
        print("\nSorry, this calculator does not support that amount of classes. ")

elif chooseCalc == "Unweighted Grade Point Average" or "unweighted grade point average" or "UNWEIGHTED GRADE POINT " \
                                                                                           "AVERAGE":

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

elif chooseCalc == "Weighted Grade Point Average" or "weighted grade point average" or "WEIGHTED GRADE POINT AVERAGE":

    numOfClasses = int(input("\nEnter your number of classes: \n"))
    honorsClasses = input("\nDo you have any Honors or AP classes? \n")

    if numOfClasses == 4 and honorsClasses == "yes" or "Yes" or "yEs" or "yeS" or "YEs" or "yES" or "YeS" or "YES":

        numOfHonClasses = int(input("\nHow many Honors or AP classes do you have? \n"))

        if numOfHonClasses == 1:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            grade1 = float(input("Enter the percentage of your first regular class: \n"))
            grade2 = float(input("Enter the percentage of your second regular class: \n"))
            grade3 = float(input("Enter the percentage of your third regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

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

            totalPtGrade = int(HonGradePt) + int(gradePt1) + int(gradePt2) + int(gradePt3)

            GPA = totalPtGrade / 4

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 2:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            grade2 = float(input("Enter the percentage of your first regular class: \n"))
            grade3 = float(input("Enter the percentage of your second regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

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

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(gradePt2) + int(gradePt3)

            GPA = totalPtGrade / 4

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 3:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            grade3 = float(input("Enter the percentage of your first regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

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

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(gradePt3)

            GPA = totalPtGrade / 4

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 4:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            HonGrade3 = float(input("Enter the percentage of your fourth Honors or AP class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

            if HonGrade3 >= 90 and HonGrade3 <= 100:
                HonGradePt3 = 5
            elif HonGrade3 >= 80 and HonGrade3 <= 89.9:
                HonGradePt3 = 4
            elif HonGrade3 >= 70 and HonGrade3 <= 79.9:
                HonGradePt3 = 3
            elif HonGrade3 >= 60 and HonGrade3 <= 69.9:
                HonGradePt3 = 2
            else:
                HonGradePt3 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(HonGradePt3)

            GPA = totalPtGrade / 4

            print("\nYour GPA is: " + str(GPA))

        else:
            print("\nThis calculator does not support that amount of Honors or AP Classes.")


    elif numOfClasses == 6 and honorsClasses == "yes" or "Yes" or "yEs" or "yeS" or "YEs" or "yES" or "YeS" or "YES":

        numOfHonClasses = int(input("\nHow many Honors or AP classes do you have? \n"))

        if numOfHonClasses == 1:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            grade1 = float(input("Enter the percentage of your first regular class: \n"))
            grade2 = float(input("Enter the percentage of your second regular class: \n"))
            grade3 = float(input("Enter the percentage of your third regular class: \n"))
            grade4 = float(input("Enter the percentage of your fourth regular class: \n"))
            grade5 = float(input("Enter the percentage of your fifth regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

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

            if grade4 >= 90 and grade4 <= 100:
                gradePt4 = 4
            elif grade4 >= 80 and grade4 <= 89.9:
                gradePt4 = 3
            elif grade4 >= 70 and grade4 <= 79.9:
                gradePt4 = 2
            elif grade4 >= 60 and grade4 <= 69.9:
                gradePt4 = 1
            else:
                gradePt4 = 0

            if grade5 >= 90 and grade5 <= 100:
                gradePt5 = 4
            elif grade5 >= 80 and grade5 <= 89.9:
                gradePt5 = 3
            elif grade5 >= 70 and grade5 <= 79.9:
                gradePt5 = 2
            elif grade5 >= 60 and grade5 <= 69.9:
                gradePt5 = 1
            else:
                gradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(gradePt1) + int(gradePt2) + int(gradePt3) + int(gradePt4) + \
                           int(gradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 2:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            grade2 = float(input("Enter the percentage of your first regular class: \n"))
            grade3 = float(input("Enter the percentage of your second regular class: \n"))
            grade4 = float(input("Enter the percentage of your third regular class: \n"))
            grade5 = float(input("Enter the percentage of your fourth regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

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

            if grade4 >= 90 and grade4 <= 100:
                gradePt4 = 4
            elif grade4 >= 80 and grade4 <= 89.9:
                gradePt4 = 3
            elif grade4 >= 70 and grade4 <= 79.9:
                gradePt4 = 2
            elif grade4 >= 60 and grade4 <= 69.9:
                gradePt4 = 1
            else:
                gradePt4 = 0

            if grade5 >= 90 and grade5 <= 100:
                gradePt5 = 4
            elif grade5 >= 80 and grade5 <= 89.9:
                gradePt5 = 3
            elif grade5 >= 70 and grade5 <= 79.9:
                gradePt5 = 2
            elif grade5 >= 60 and grade5 <= 69.9:
                gradePt5 = 1
            else:
                gradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(gradePt2) + int(gradePt3) + int(gradePt4) + \
                           int(gradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 3:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            grade3 = float(input("Enter the percentage of your first regular class: \n"))
            grade4 = float(input("Enter the percentage of your second regular class: \n"))
            grade5 = float(input("Enter the percentage of your third regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

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

            if grade4 >= 90 and grade4 <= 100:
                gradePt4 = 4
            elif grade4 >= 80 and grade4 <= 89.9:
                gradePt4 = 3
            elif grade4 >= 70 and grade4 <= 79.9:
                gradePt4 = 2
            elif grade4 >= 60 and grade4 <= 69.9:
                gradePt4 = 1
            else:
                gradePt4 = 0

            if grade5 >= 90 and grade5 <= 100:
                gradePt5 = 4
            elif grade5 >= 80 and grade5 <= 89.9:
                gradePt5 = 3
            elif grade5 >= 70 and grade5 <= 79.9:
                gradePt5 = 2
            elif grade5 >= 60 and grade5 <= 69.9:
                gradePt5 = 1
            else:
                gradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(gradePt3) + int(gradePt4) + \
                           int(gradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 4:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            HonGrade3 = float(input("Enter the percentage of your fourth Honors or AP class: \n"))
            grade4 = float(input("Enter the percentage of your first regular class: \n"))
            grade5 = float(input("Enter the percentage of your second regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

            if HonGrade3 >= 90 and HonGrade3 <= 100:
                HonGradePt3 = 5
            elif HonGrade3 >= 80 and HonGrade3 <= 89.9:
                HonGradePt3 = 4
            elif HonGrade3 >= 70 and HonGrade3 <= 79.9:
                HonGradePt3 = 3
            elif HonGrade3 >= 60 and HonGrade3 <= 69.9:
                HonGradePt3 = 2
            else:
                HonGradePt3 = 0

            if grade4 >= 90 and grade4 <= 100:
                gradePt4 = 4
            elif grade4 >= 80 and grade4 <= 89.9:
                gradePt4 = 3
            elif grade4 >= 70 and grade4 <= 79.9:
                gradePt4 = 2
            elif grade4 >= 60 and grade4 <= 69.9:
                gradePt4 = 1
            else:
                gradePt4 = 0

            if grade5 >= 90 and grade5 <= 100:
                gradePt5 = 4
            elif grade5 >= 80 and grade5 <= 89.9:
                gradePt5 = 3
            elif grade5 >= 70 and grade5 <= 79.9:
                gradePt5 = 2
            elif grade5 >= 60 and grade5 <= 69.9:
                gradePt5 = 1
            else:
                gradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(HonGradePt3) + \
                           int(gradePt4) + int(gradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 5:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            HonGrade3 = float(input("Enter the percentage of your fourth Honors or AP class: \n"))
            HonGrade4 = float(input("Enter the percentage of your fifth Honors or AP class: \n"))
            grade5 = float(input("Enter the percentage of your first regular class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

            if HonGrade3 >= 90 and HonGrade3 <= 100:
                HonGradePt3 = 5
            elif HonGrade3 >= 80 and HonGrade3 <= 89.9:
                HonGradePt3 = 4
            elif HonGrade3 >= 70 and HonGrade3 <= 79.9:
                HonGradePt3 = 3
            elif HonGrade3 >= 60 and HonGrade3 <= 69.9:
                HonGradePt3 = 2
            else:
                HonGradePt3 = 0

            if HonGrade4 >= 90 and HonGrade4 <= 100:
                HonGradePt4 = 5
            elif HonGrade4 >= 80 and HonGrade4 <= 89.9:
                HonGradePt4 = 4
            elif HonGrade4 >= 70 and HonGrade4 <= 79.9:
                HonGradePt4 = 3
            elif HonGrade4 >= 60 and HonGrade4 <= 69.9:
                HonGradePt4 = 2
            else:
                HonGradePt4 = 0

            if grade5 >= 90 and grade5 <= 100:
                gradePt5 = 4
            elif grade5 >= 80 and grade5 <= 89.9:
                gradePt5 = 3
            elif grade5 >= 70 and grade5 <= 79.9:
                gradePt5 = 2
            elif grade5 >= 60 and grade5 <= 69.9:
                gradePt5 = 1
            else:
                gradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(HonGradePt3) + int(
                HonGradePt4) + int(gradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        elif numOfHonClasses == 6:

            HonGrade = float(input("\nEnter the percentage of your first Honors or AP class: \n"))
            HonGrade1 = float(input("Enter the percentage of your second Honors or AP class: \n"))
            HonGrade2 = float(input("Enter the percentage of your third Honors or AP class: \n"))
            HonGrade3 = float(input("Enter the percentage of your fourth Honors or AP class: \n"))
            HonGrade4 = float(input("Enter the percentage of your fifth Honors or AP class: \n"))
            HonGrade5 = float(input("Enter the percentage of your sixth Honors or AP class: \n"))

            if HonGrade >= 90 and HonGrade <= 100:
                HonGradePt = 5
            elif HonGrade >= 80 and HonGrade <= 89.9:
                HonGradePt = 4
            elif HonGrade >= 70 and HonGrade <= 79.9:
                HonGradePt = 3
            elif HonGrade >= 60 and HonGrade <= 69.9:
                HonGradePt = 2
            else:
                HonGradePt = 0

            if HonGrade1 >= 90 and HonGrade1 <= 100:
                HonGradePt1 = 5
            elif HonGrade1 >= 80 and HonGrade1 <= 89.9:
                HonGradePt1 = 4
            elif HonGrade1 >= 70 and HonGrade1 <= 79.9:
                HonGradePt1 = 3
            elif HonGrade1 >= 60 and HonGrade1 <= 69.9:
                HonGradePt1 = 2
            else:
                HonGradePt1 = 0

            if HonGrade2 >= 90 and HonGrade2 <= 100:
                HonGradePt2 = 5
            elif HonGrade2 >= 80 and HonGrade2 <= 89.9:
                HonGradePt2 = 4
            elif HonGrade2 >= 70 and HonGrade2 <= 79.9:
                HonGradePt2 = 3
            elif HonGrade2 >= 60 and HonGrade2 <= 69.9:
                HonGradePt2 = 2
            else:
                HonGradePt2 = 0

            if HonGrade3 >= 90 and HonGrade3 <= 100:
                HonGradePt3 = 5
            elif HonGrade3 >= 80 and HonGrade3 <= 89.9:
                HonGradePt3 = 4
            elif HonGrade3 >= 70 and HonGrade3 <= 79.9:
                HonGradePt3 = 3
            elif HonGrade3 >= 60 and HonGrade3 <= 69.9:
                HonGradePt3 = 2
            else:
                HonGradePt3 = 0

            if HonGrade4 >= 90 and HonGrade4 <= 100:
                HonGradePt4 = 5
            elif HonGrade4 >= 80 and HonGrade4 <= 89.9:
                HonGradePt4 = 4
            elif HonGrade4 >= 70 and HonGrade4 <= 79.9:
                HonGradePt4 = 3
            elif HonGrade4 >= 60 and HonGrade4 <= 69.9:
                HonGradePt4 = 2
            else:
                HonGradePt4 = 0

            if HonGrade5 >= 90 and HonGrade5 <= 100:
                HonGradePt5 = 5
            elif HonGrade5 >= 80 and HonGrade5 <= 89.9:
                HonGradePt5 = 4
            elif HonGrade5 >= 70 and HonGrade5 <= 79.9:
                HonGradePt5 = 3
            elif HonGrade5 >= 60 and HonGrade5 <= 69.9:
                HonGradePt5 = 2
            else:
                HonGradePt5 = 0

            totalPtGrade = int(HonGradePt) + int(HonGradePt1) + int(HonGradePt2) + int(HonGradePt3) + \
                           int(HonGradePt4) + int(HonGradePt5)

            GPA = totalPtGrade / 6

            print("\nYour GPA is: " + str(GPA))

        else:
            print("\nThis calculator does not support that amount of Honors or AP Classes.")


    elif numOfClasses == 4 and honorsClasses == "no" or "No" or "nO" or "NO":

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

    elif numOfClasses == 6 and honorsClasses == "no" or "No" or "nO" or "NO":

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

        if grade4 >= 90 and grade4 <= 100:
            gradePt4 = 4
        elif grade4 >= 80 and grade4 <= 89.9:
            gradePt4 = 3
        elif grade4 >= 70 and grade4 <= 79.9:
            gradePt4 = 2
        elif grade4 >= 60 and grade4 <= 69.9:
            gradePt4 = 1
        else:
            gradePt4 = 0

        if grade5 >= 90 and grade5 <= 100:
            gradePt5 = 4
        elif grade5 >= 80 and grade5 <= 89.9:
            gradePt5 = 3
        elif grade5 >= 70 and grade5 <= 79.9:
            gradePt5 = 2
        elif grade5 >= 60 and grade5 <= 69.9:
            gradePt5 = 1
        else:
            gradePt5 = 0

        totalPtGrade = int(gradePt) + int(gradePt1) + int(gradePt2) + int(gradePt3) + int(gradePt4) + int(gradePt5)

        GPA = totalPtGrade / 6

        print("\nYour GPA is: " + str(GPA))

    else:
        print("\nSorry, this calculator does not support that amount of classes.")

else:
    print("\nSorry, we do not have that calculator available.")
