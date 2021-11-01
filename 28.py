class time:
    def __init__(self,seconds):
        self.seconds=seconds
    def convert_to_ms(self):
        minutes=self.seconds//60
        seconds=self.seconds%60
        return (str(minutes)+":"+str(seconds))
    def convert_to_hms(self):
        hours=self.seconds//3600
        rm=self.seconds-hours*3600
        minutes=rm//60
        seconds=rm%60
        return (str(hours)+":"+ str(minutes)+":"+ str(seconds))
a=int(input("enter seconds"))
c=time(a)
print("time in minutes and seconds--->",c.convert_to_ms())
print("time in hours,minutes and seconds-->",c.convert_to_hms())
    
