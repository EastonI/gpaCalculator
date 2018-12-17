# This is my Main Algorithm
# Abstraction
# Parent Abstraction is in Orange Rectangle
# Sub Abstractions are in red rectangles

from FinalishCode.GradePercentAverage import gpera
from FinalishCode.UnweightedGPA import ugpa
from FinalishCode.WeightedGPA import wgpa

print("GPA Calculators")

chooseCalc = input("\nWould you like to calculate your GPeA, UGPA, or your WGPA? \n")

if chooseCalc == "WGPA":
    print("\nWeighted Grade Point Average Calculator")
    wgpa()

elif chooseCalc == "wgpa":
    print("\nWeighted Grade Point Average Calculator")
    wgpa()

elif chooseCalc == "UGPA":
    print("\nUnweighted Grade Point Average Calculator")
    ugpa()

elif chooseCalc == "ugpa":
    print("\nUnweighted Grade Point Average Calculator")
    ugpa()

elif chooseCalc == "GPeA":
    print("\nGrade Percent Average Calculator")
    gpera()

elif chooseCalc == "GPEA":
    print("\nGrade Percent Average Calculator")
    gpera()

elif chooseCalc == "gpea":
    print("\nGrade Percent Average Calculator")
    gpera()

else:
    print("\nSorry, we do not have that calculator available.")
