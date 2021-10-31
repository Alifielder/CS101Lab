import math
prgrm=[]
tst=[]
total_Scores=[]
def getAverage(total_Scores):
    tsLeng=len(total_Scores)
    classTotal=0
    for x in range(0,tsLeng):
        classTotal=classTotal+total_Scores[x]
        return (classTotal/tsLeng)

def display():    
    tsLeng=len(total_Scores)
    standardDev=0   
    classTotal=0
    average=getAverage(total_Scores)
    for x in range(0,tsLeng):
        #𝑠𝑡𝑑=√((value−mean)^2+(value−mean)^2+(value−mean)^2+(value−mean)^2)/4
        standardDev=total_Scores[x]-average
        classTotal=classTotal+(standardDev*standardDev)
        classTotal=classTotal/4
        classTotal=math.sqrt(classTotal)
        return classTotal
    progmin=min(prgrm)
    testmin=min(tst)
    tsLeng=len(tst)
    testmax=max(tst)
    progMax=max(prgrm)
    testaverage=getAverage(tst)
    progAverage=getAverage(tst)
    progLeng=len(prgrm)
    progStdDev=standardDev
    teststandardDev=standardDev
    #finish defining variables
    print('Type               #       min       max       avg       std\n============================================================\nTests              ',str(tsLeng),'       ',testmin,'     ',testmax,'   ',testaverage,'      ',teststandardDev,'\nPrograms          ',str(progLeng),'       ',progmin,'       ',progMax,'       ',progAverage,'       ',progStdDev,'\nThe weighted scores is       ',classTotal)
def menu():
    while(1):
        user_Options=input('1:Add Test\n2:Remove Test\n3:Clear Test\n4:Add Assignment\n5:Remove Assignment\n6:Clear Assignment\n7:Display\n8:Quit\n')
        if user_Options==("1"):
            user_AddTest=int(input("Score on test:"))
            if user_AddTest>=0 and user_AddTest<=100:
                tst.append(user_AddTest)
                continue
        elif user_Options==('2'):
            user_RemoveTest=int(input('Score on test: '))
            for x in range(len(tst)):
                if tst[x]==user_RemoveTest:
                    tst.remove(user_RemoveTest)
                elif x==len(tst)-1:
                    print("Test isn't there, cannot remove it")
        elif user_Options==('3'):
            tst.clear()
        elif user_Options==('4'):
            user_AddProg=int(input("Score on Assignment:"))
            if user_AddProg>=0 & user_AddProg<=100:
                prgrm.append(user_AddProg)
                continue
        elif user_Options==('5'):
            user_RemoveProg=int(input('Score on Assignment: '))
            for x in range(len(prgrm)):
                if prgrm[x]==user_RemoveProg:
                    prgrm.remove(user_RemoveProg)
                    continue
                elif x==len(prgrm)-1:
                    print("Assignment isn't there, cannot remove it")
                    continue
        elif user_Options==('6'):
            prgrm.clear()
        elif user_Options==('7'):
            display()
        elif user_Options==('8'):
            print('Goodbye')
            break
def main():
    print(menu())
main()