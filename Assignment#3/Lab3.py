def getRemain(num):
    while(True):
        rem=int(input('What is the remainder when your number is divided by '+str(num)+'?:'))
        if(rem<0):
            print("The remainder should be greater than 0")
        elif(rem>=num):
            print("The remainder should be less than",num)
        else:
            return rem
def getGuess(rema3,rema5,rema7):
    for i in range(1,111):
        if(i%3==rema3 and i%5==rema5 and i%7==rema7):
            return i
three=3
five=5
seven=7
while(True):
    print("Please think of a number between 1 and 100 in your head...")
    r_3=getRemain(three)
    r_5=getRemain(five)
    r_7=getRemain(seven)
    guess=getGuess(r_3,r_5,r_7)
    print('Your number was:', guess,'\nHow amazing is that!')
    while(True):
        goAgain=input("Do you want to play again? To continue: Type Y , To quit: Type N: ")
        if(goAgain=='Y'or goAgain=='y'):
            break
        elif(goAgain=="n" or goAgain=="N"):
            break
        print()
