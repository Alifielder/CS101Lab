#gathering input statements
#welcome statement
print('Welcome to the LAB grade calculator!')
userName=input('Who are we calculating grades for? ==>')
labGrade=float(input('Enter the Labs grade? ==>'))
examGrade=float(input('Enter the EXAMS grade? ==>'))
attGrade=float(input('Enter the attendance grade? ==>'))
#if/else for grade input range 0-100
if(0<labGrade<100):
    weightedLab= labGrade+(labGrade*.7)
elif(0>labGrade):
    print('The lab grade must be zero or greater. It has been changed to zero.')
    labGrade=0
    weightedLab= labGrade+(labGrade*.7)
elif(100<labGrade):
    print('The lab grade must be 100 or less. It has been changed to 100.')
    labGrade=100
    weightedLab= labGrade+(labGrade*.7)
if(0<attGrade<100):
    weightedAtt= attGrade+(attGrade*.1)
elif(0>attGrade):
    print('The att grade must be zero or greater. It has been changed to zero.')
    attGrade=0
    weightedAtt= attGrade+(attGrade*.1)
elif(100<attGrade):
    print('The att grade must be 100 or less. It has been changed to 100.')
    attGrade=100
    weightedAtt= attGrade+(attGrade*.1)
if(0<examGrade<100):
    weightedExam= examGrade+(examGrade*.2)
elif(0>examGrade):
    print('The exam grade must be zero or greater. It has been changed to zero.')
    examGrade=0
    weightedExam= examGrade+(examGrade*.2)
elif(100<examGrade):
    print('The exam grade must be 100 or less. It has been changed to 100.')
    examGrade=100
    weightedExam= examGrade+(examGrade*.2)
#combining grades
weightedTotal = (weightedLab+weightedExam+weightedAtt)/3
#assigning letter value to numeric grade
if(90<=weightedTotal<=100):
    print('The weighted grade for', userName,'is',weightedTotal,'\n ',userName,' has a letter grade of A')
elif(80<=weightedTotal<=89):
    print('The weighted grade for', userName,'is',weightedTotal,'\n ',userName,' has a letter grade of B')
elif(70<=weightedTotal<=79):
    print('The weighted grade for', userName,'is',weightedTotal,'\n ',userName,' has a letter grade of C')
elif(60<=weightedTotal<=69):
    print('The weighted grade for', userName,'is',weightedTotal,'\n ',userName,' has a letter grade of D')
elif(weightedTotal<=59):
    print('The weighted grade for', userName,'is',weightedTotal,'\n ',userName,' has a letter grade of F')
