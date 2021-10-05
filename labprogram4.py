import random
from types import resolve_bases
reela=int
reelb=int
reelc=int
def play_again():
    while(True):
        again=input('Would you like to play again? Y for yes N for no')
        if(again=="Y"):
            return True
        elif(again=="N"):
            return False
        else:
            print("You must enter Y to continue or N to end!")
def get_wager(bank:int):
    chip_wager_Input=int(input('How many chips would you like to wager'))
    while(True):
        if chip_wager_Input<=0:
            print('The chips you wager must be greater than 0')
        elif chip_wager_Input>=bank:
            print('Your chip wager must be less than or equal to the bank!')
        else:
            return chip_wager_Input
def get_slot_results():
    reela=int(random.random()*10)
    reelb=int(random.random()*10)
    reelc=int(random.random()*10)
    return (reela,reelb,reelc)
def get_matches(reela,reelb,reelc):
    while True:
        if (reela!=reelb and reela!=reelc and reelb!=reelc):
            return 0
        elif (reela==reelb and reelb==reelc):
            return 3
        else:
            return 2
def get_bank():
    while(True):
        start_input=int(input("How many chips would you like to start with?"))
        if(start_input<=0):
            print("Please enter a larger number, between 1-100")
        elif(start_input>100):
            print("Please enter a smaller number, between 1-100")
        else:
            return start_input
def get_payout(wager,matches):
    if(matches==0):
        return wager*-1
    elif(matches==2):
        return wager*5
    else:
        return wager*10
if __name__=="__main__":
    playing=True
    while(playing):
        bank=get_bank()
        turns=0
        initialBank=bank
        while(bank>0):
            wager=get_wager(bank)
            matches=get_matches(reela,reelb,reelc)
            payout=get_payout(wager,matches)
            bank=bank+payout
            print('Your spin:',reela,reelb,reelc)
            print('You matched:',matches)
            print('You won/lost:',payout)
            print('Current bank:',bank)
            turns+=1
        playing=play_again()    
