"c:\bill\gettysburg.txt"
"c:\bill\test.txt"
while True:
    getUserfile=input("Enter a file to open:\n")
    try:
        userTest=open(getUserfile)

        wordDiction=dict()
        for line in userTest:
            for word in line.strip().split(''):
                word=word.strip(",")
                if len(word)<=3:
                    continue
                else:
                    if word in wordDiction.keys():
                        wordDiction[word]=wordDiction[word]+1
                    else:
                        wordDiction[word]=1
        wordDiction=dict(sorted(wordDiction.items(),key,reverse=True))
        counter=1
        print('Most frequent words')
        print("{:>0}{:>15}{:>15}".format('#','Word','Freq'))
        print('{:>15}'.format("====================="))
        for key in wordDiction:
            if counter>10:
                break
            else:
                frequency=wordDiction[key]
                print("{:>0}{:>15}{:>15}".format('#','Word','Freq'))
                counter+=1
            oneOccCount=0
            for key in wordDiction:
                if wordDiction[key]==1:
                    oneOccCount+=1
            UniqueC=len(wordDiction)
            print('There are',oneOccCount,'Words that occur only once\nThere are',UniqueC,'unique words in the file')
    except:
        print('Could not open file: ',getUserfile,"Try again\n")
        continue
    else:
        break


