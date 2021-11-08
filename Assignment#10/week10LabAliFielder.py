import csv
def month_from_number(n):
    calendar = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
    return calendar[str(n)]
def read_in_file(KCPDCrimeData):
    dataList = []
    f = open("KCPDCrimeData.csv",encoding='UTF-8')
    reader = csv.reader(f)
    for row in reader:
        dataList.append(row)
    f.close()
    return dataList
def create_reported_date_dict(read_in_file):
    read_in_file()
    key_count=0
    for key in dataList:
        try:
            key_count[key]+=1
        except KeyError:
            key_count[key]=1
def create_offense_dict(dataList):
    return create_offense_dict(dataList,"Offense")
def create_offense_by_zip(dataList):
    dict_ex={}
    for sub in dataList[1:]:
        temp = sub[7]
        if temp in dict_ex:
            temp_dict = dict_ex[temp]
            if sub[13] in temp_dict:
                temp_dict[sub[13]]+=1
            else:
                temp_dict[sub[13]] = 1
        else:
            dict_ex[temp] = {sub[13]:1}
    return dict_ex
def create_reported_month_dict():
    month=create_reported_month_dict(dataList)
    month
def main():
    while(True):
        user_file = input("Enter the name of the crime data file ==> ")
        dataList = read_in_file(user_file)
        if(dataList==-1):
            print("Could not find the file specified. "+user_file+" not found")
        else:
            break
    create_reported_month_dict()
    print(month)
    maxx = max(month,key=month.get)
    print("The month with the highest # of crimes is "+month_from_number(maxx)+" with "+str(month[maxx])+" offenses")
    offense = create_offense_dict(dataList)
    offense_Key=offense.get
    maxx = max(offense,offense_Key)
    print("The offense with the highest # of crimes is "+maxx+" with "+str(offense[maxx])+" offenses")
    offense = create_offense_by_zip(dataList)
    print()
    while(True):
        off = input("Enter an offense : ")
        if off not in offense:
            print("Not a valid offense, please try again")
        else:
            break
    print(off+" offense by Zip Code")
    print("Zip Code\                       # Offenses")
    print("==========================================")
    for k,v in offense[off].items():
        print(k+"\t\t\t\t\t"+str(v))

if __name__ == "__main__":
    main()