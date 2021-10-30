
list1=[]
list2=[]
while(1):
    try:
        minimum_mpg=float(input('Enter the minimum MPG: '))
        if(minimum_mpg<0):
            print('Fuel economy must be greater than zero (0)!')
        elif(minimum_mpg>100):
            print('Fuel economy must be less than one hundred (100)!')
        else:
            break
    except ValueError:
        print("You must enter a number for the fuel economy")
        continue
while(1):
    try:
        fileIN=(input('Enter the name of input vehicle file: '))

        file=open(fileIN,'r')
        for i in file:
            list1.append(i.split())
        break
    except FileNotFoundError:
        print('Could not open file',fileIN)
        continue
while(1):
    try:
        fileOUT=(input('Enter the name of the output file: '))
        file2=open(fileOUT,'w')
        break
    except IOError:
        print('There is an IO Error', fileOUT)
        continue
for i in range(len(list1)):
    try:
        a=list1[i][0]
        b=list1[i][1]
        c=list1[i][2]
        d=list1[i][7]
        if(int(d)>minimum_mpg):
            fileOUT.write("{:<40}{:<40}{:<40}{:>10}\n".format(a,b,c,d))
    except:
        print("Could not convert value {} for vehicle {} {} {}".format(d,a,b,c))        
    continue