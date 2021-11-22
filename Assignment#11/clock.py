import time
class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.minute=minute
        self.hour=hour
        self.second=second
        if second>=60:
            raise ValueError("Seconds cannot be greater than 59")
        elif second<0:
            raise ValueError("Seconds cannot be less than 0")
        elif minute>=60:
            raise ValueError("Minutes cannot be greater than 59")
        elif minute<0:
            raise ValueError("Minutes cannot be less than 0")
        elif hour>=24:
            raise ValueError("Hours cannot be greater than 59")
        elif hour<0:
            raise ValueError("Hours cannot be less than 0")
    def tick(self,second,hour,minute):
        self.second+=1
        if second==59:
            minute+=1
            if  minute==59:
                hour+=1
                if hour==23:
                    second=0
                    minute=0
                    hour=0   
    def __str__(self):
        hourOut=self.hour
        minuteOut=self.minute
        secondOut=self.second    
        clock_type()
    
    def clock_type(self,minute,hour,second):
        user_clockType=input("24 Hour clock or 12 Hour clock: \n")
        if user_clockType=="24":
            print("12/ AM/PM Clock")
        elif user_clockType=="12":
            print("24 Hour Clock")
        else:
            print("Enter a different clock type")
        if hourOut < 12:
            if hourOut == 0:
                hourPrint = 12
                time = f"{hourOut:02}:{minuteOut:02}:{secondOut:02} am"
            else:
                if hourPrint > 12:
                    time = f"{hourOut:02}:{minuteOut:02}:{secondOut:02} pm"
        else:
            time = f"{hourOut:02}:{minuteOut:02}:{secondOut:02}"
        return time
    if __name__=="__main__":
        hour=int(input("Current Hour: \n"))
        minute=int(input("Current Minute: \n"))
        second=int(input("Current Second:  \n"))
        clockOption=Clock(hour,minute,second)
        while True:
            print(clockOption)
            clockOption.tick()
            clockOption.__str__()
            time.sleep(1)